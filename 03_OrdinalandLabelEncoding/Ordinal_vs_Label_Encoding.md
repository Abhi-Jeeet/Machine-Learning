# Ordinal Encoding and Label Encoding

## 1. Label Encoding

### What is Label Encoding?

Label Encoding converts categorical values into numerical labels (0, 1,
2, 3, ...). Each unique category gets a number.

### Example

  Color   Encoded
  ------- ---------
  Red     0
  Blue    1
  Green   2

Here, categories are simply assigned numbers.

### Python Example

``` python
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
colors = ["Red", "Blue", "Green", "Blue"]
encoded = le.fit_transform(colors)
print(encoded)
```

### When to Use Label Encoding?

-   When encoding the target variable (y) in classification.
-   When categories have only two classes (binary classification).

### Problem

Label Encoding introduces false ordering.

Example:

  City      Encoded
  --------- ---------
  Delhi     0
  Mumbai    1
  Chennai   2

The model may think Chennai \> Mumbai \> Delhi, but cities have no
natural order.

------------------------------------------------------------------------

## 2. Ordinal Encoding

### What is Ordinal Encoding?

Ordinal Encoding is used when categories have a natural order.

Examples: - Low \< Medium \< High - Small \< Medium \< Large - Poor \<
Average \< Good \< Excellent

### Example

  Size     Encoded
  -------- ---------
  Small    0
  Medium   1
  Large    2

Here the order makes sense.

### Python Example

``` python
from sklearn.preprocessing import OrdinalEncoder
import numpy as np

data = np.array([["Small"], ["Medium"], ["Large"]])

oe = OrdinalEncoder(categories=[["Small", "Medium", "Large"]])
encoded = oe.fit_transform(data)
print(encoded)
```

### When to Use Ordinal Encoding?

-   When categorical data has ranking or order.
-   When order matters in real life.

Examples: - Education Level (High School \< Graduate \< Postgraduate) -
Customer Satisfaction (Low \< Medium \< High)

------------------------------------------------------------------------

## Key Differences

  Feature            Label Encoding           Ordinal Encoding
  ------------------ ------------------------ -----------------------------
  Used For           Mostly target variable   Input features with order
  Order Important?   No                       Yes
  Risk               Creates false ranking    Correctly preserves ranking
  Classes            Binary or multi-class    Ordered categories

------------------------------------------------------------------------

## Important Interview Points

-   If categories have NO order → Use One-Hot Encoding.
-   If categories have ORDER → Use Ordinal Encoding.
-   If encoding target variable → Use Label Encoding.

------------------------------------------------------------------------

## Real Example in ML

If predicting salary:

Education = \["High School", "Graduate", "Postgraduate"\]\
Order exists → Use Ordinal Encoding.

City = \["Delhi", "Mumbai", "Chennai"\]\
No order → Use One-Hot Encoding.
