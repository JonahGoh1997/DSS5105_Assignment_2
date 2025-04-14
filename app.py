#####################################################################
#### app.py ####

from flask import Flask, request, jsonify
import statsmodels.api as sm
import numpy as np

app = Flask(__name__)

# Training data
# Dataset: [Treatment (W), Sustainability Spending (X)]
X_data = np.array([
    [0, 19.8],
    [1, 23.4],
    [1, 27.7],
    [1, 24.6],
    [0, 21.5],
    [1, 25.1],
    [1, 22.4],
    [0, 29.3],
    [0, 20.8],
    [1, 20.2],
    [1, 27.3],
    [0, 24.5],
    [0, 22.9],
    [1, 18.4],
    [0, 24.2],
    [1, 21.0],
    [0, 25.9],
    [0, 23.2],
    [1, 21.6],
    [1, 22.8]
])

# Engagement Score (Y^obs)
y_data = np.array([
    137, 118, 124, 124, 120, 129, 122, 142, 128, 114,
    132, 130, 130, 112, 132, 117, 134, 132, 121, 128
])

# Add intercept (constant)
X_data_sm = sm.add_constant(X_data)

# Fit model using statsmodels for statistical significance
model = sm.OLS(y_data, X_data_sm).fit()

# Extract coefficients
alpha = model.params[0]      # Intercept
tau = model.params[1]        # Coefficient of W (treatment)
beta = model.params[2]       # Coefficient of X (sustainability spending)

# Extract ATE (τ) p-value
tau_pval = model.pvalues[1]   # p-value of Treatment

@app.route("/ate")
def get_ate():
    return jsonify({
        "alpha (Intercept)": round(alpha, 4),
        "ATE (tau)": round(tau, 4),
        "beta (Sustainability Spending effect)": round(beta, 4),
        "ATE (tau) p-value": round(tau_pval, 4),
        "Interpretation": "Not statistically significant" if tau_pval > 0.05 else "Statistically significant"
    })

@app.route("/predict")
def predict():
    try:
        # Get query parameters
        w = float(request.args.get("w"))
        x = float(request.args.get("x"))

        # Construct input vector with intercept
        input_vector = [1, w, x]  # [alpha, W, X]
        prediction = model.predict([input_vector])[0]

        return jsonify({
            "Input": {"W": w, "X": x},
            "Predicted Engagement Score": round(prediction, 2)
        })

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
