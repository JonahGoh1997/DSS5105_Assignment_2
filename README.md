# DSS5105 Assignment 2 – Flask ATE Model API

This project implements a Flask web application that fits a linear regression model to estimate the **Average Treatment Effect (ATE)** using observational data. The app exposes two endpoints:

- `/ate`: Returns model coefficients (α, τ, β) and the statistical significance of the treatment effect.
- `/predict`: Returns the predicted engagement score for given treatment and sustainability spending inputs.

## 📈 Model Specification

The linear model is defined as:

```
Y = α + τ·W + β·X + ε
```

Where:
- `Y` = Engagement Score  
- `W` = Treatment (0 or 1)  
- `X` = Sustainability Spending  
- `α` = Intercept  
- `τ` = Average Treatment Effect (ATE)  
- `β` = Effect of sustainability spending  

## 🚀 Getting Started

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the app

```bash
python app.py
```

Server will start on: `http://localhost:5000`

## 🔌 API Endpoints

### `/predict` – Predict engagement score

**Usage:**

```bash
curl "http://localhost:5000/predict?w=1&x=25.0"
```

**Response:**

```json
{
  "Input": {"W": 1.0, "X": 25.0},
  "Predicted Engagement Score": 124.73
}
```

### `/ate` – View model coefficients and ATE significance

**Usage:**

```bash
curl http://localhost:5000/ate
```

**Response:**

```json
{
  "ATE (tau)": -9.1057,
  "ATE (tau) p-value": 0.0004,
  "Interpretation": "Statistically significant",
  "alpha (Intercept)": 95.9662,
  "beta (Sustainability Spending effect)": 1.5149
}
```

## 📦 Dependencies

This project uses the following Python packages:

- Flask
- numpy
- statsmodels

All dependencies are listed in `requirements.txt`.

## 👤 Author

[@JonahGoh1997](https://github.com/JonahGoh1997)
