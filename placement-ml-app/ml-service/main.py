from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import joblib
import numpy as np

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

model = joblib.load("placementModel.pkl")
scaler = joblib.load("scaler.pkl")   # 🔥 Load scaler too

@app.post("/predict")
def predict(data: dict):
    iq = data["iq"]
    cgpa = data["cgpa"]

    # Validate input range
    if not isinstance(iq, (int, float)) or not isinstance(cgpa, (int, float)):
        raise HTTPException(status_code=400, detail="IQ and CGPA must be numbers")
    
    if iq < 1 or iq > 10 or cgpa < 1 or cgpa > 10:
        raise HTTPException(status_code=400, detail="IQ and CGPA must be between 1 and 10")

    features = np.array([[iq, cgpa]])

    # 🔥 Apply same scaling used during training
    scaled_features = scaler.transform(features)

    prediction = model.predict(scaled_features)[0]
    probability = model.predict_proba(scaled_features)[0][1]

    return {
        "prediction": int(prediction),
        "probability": float(probability)
    }
