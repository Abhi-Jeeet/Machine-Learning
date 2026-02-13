const express = require("express");
const axios = require("axios");
const cors = require("cors");

const app = express();

app.use(express.json());
app.use(cors());

app.post("/predict", async (req, res) => {
  try {
    const { iq, cgpa } = req.body;

    // Validate input range
    if (typeof iq !== "number" || typeof cgpa !== "number") {
      return res.status(400).json({ error: "IQ and CGPA must be numbers" });
    }

    if (iq < 1 || iq > 10 || cgpa < 1 || cgpa > 10) {
      return res
        .status(400)
        .json({ error: "IQ and CGPA must be between 1 and 10" });
    }

    const response = await axios.post(
      "http://localhost:8000/predict",
      req.body,
    );

    res.json(response.data);
  } catch (error) {
    res.status(500).json({ error: "ML Service Error" });
  }
});

app.listen(3000, () => {
  console.log("Node server running on http://localhost:3000");
});
