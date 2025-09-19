import os
import pandas as pd
import numpy as np

# Input and output paths
in_path = os.path.join("data", "Standardization", "kpi_minmax_scaled.csv")
out_dir = os.path.join("data", "weights", "entropy")
os.makedirs(out_dir, exist_ok=True)
weights_path = os.path.join(out_dir, "kpi_weights.csv")

# Load normalized data
df = pd.read_csv(in_path, parse_dates=["date"])

# KPI columns
kpi_cols = [
    "net_sales_adj",             # Net Sales
    "margin_pct",                # Margin
    "nps",                       # NPS
    "sales_new_pct_of_sales",    # Sales from New Products
    "pm_refrigerator_pct",       # Product Mix - Refrigerator
    "pm_washer_pct",             # Product Mix - Washer
    "pm_oven_pct",               # Product Mix - Oven
    "pm_other_pct"               # Product Mix - Other
]

# Extract normalized data
X = df[kpi_cols].values  

# Check for NaN or negative values
if np.any(np.isnan(X)) or np.any(X < 0):
    print("Error: Data contains NaN or negative values.")
    print("NaN count:", np.sum(np.isnan(X)))
    print("Negative values count:", np.sum(X < 0))
    raise ValueError("Data contains NaN or negative values. Please check the normalized data.")

# Calculate Entropy weights
# Step 1: Normalize data to sum to 1 for each KPI
X_sum = np.sum(X, axis=0)
X_sum[X_sum == 0] = 1e-10  # Avoid division by zero
P = X / X_sum 

# Step 2: Calculate entropy for each KPI
k = 1 / np.log(len(X))  
P = np.where(P == 0, 1e-10, P)  # Replace 0 with small value to avoid log(0)
entropy = -k * np.sum(P * np.log(P), axis=0)

# Step 3: Calculate weights
weights = (1 - entropy) / np.sum(1 - entropy)

# Create a DataFrame for weights
weights_df = pd.DataFrame({
    'KPI': kpi_cols,
    'Weight': weights
})

# Save results
weights_df.to_csv(weights_path, index=False)

# Print results
print("Entropy Weights:")
print(weights_df)
print("\nWeights saved to:", weights_path)