import os
import pandas as pd
import numpy as np

# Input and output paths
in_path = os.path.join("data", "Standardization", "kpi_minmax_scaled.csv")
out_dir = os.path.join("data", "weights", "critic")
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

# Calculate CRITIC weights
# Step 1: Calculate standard deviation for each criterion
std_dev = np.std(X, axis=0)

# Step 2: Calculate correlation matrix
corr_matrix = np.corrcoef(X.T)

# Step 3: Calculate conflict measure (C_j) for each criterion
n_criteria = X.shape[1]
conflict = np.zeros(n_criteria)
for j in range(n_criteria):
    for k in range(n_criteria):
        if j != k:
            conflict[j] += (1 - abs(corr_matrix[j, k]))

# Step 4: Calculate weights
weights = (std_dev * conflict) / np.sum(std_dev * conflict)

# Create a DataFrame for weights
weights_df = pd.DataFrame({
    'KPI': kpi_cols,
    'Weight': weights
})

# Save results
weights_df.to_csv(weights_path, index=False)

# Print results
print("CRITIC Weights:")
print(weights_df)
print("\nWeights saved to:", weights_path)