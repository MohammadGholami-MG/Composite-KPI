import pandas as pd
import os
from sklearn.preprocessing import MinMaxScaler

# Input and output paths
in_path = os.path.join("data","dummy","data_adjusted.csv")
out_dir = os.path.join("data", "Standardization")
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, "kpi_minmax_scaled.csv")

# Load dataset
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

# Apply Min-Max Scaling to bring all values between 0 and 1
scaler = MinMaxScaler()
df_scaled = df.copy()
df_scaled[kpi_cols] = scaler.fit_transform(df[kpi_cols])

# Save result
df_scaled.to_csv(out_path, index=False)

print(f"Min-Max scaled data saved to: {out_path}")
print(df_scaled.head().to_string(index=False))
