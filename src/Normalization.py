import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler

# Load raw data
file_path = os.path.join("data","dummy","data_adjusted.csv")
df = pd.read_csv(file_path, parse_dates=["date"])

# Create output directory
out_dir = os.path.join("data", "normalized")
os.makedirs(out_dir, exist_ok=True)

# Normalization methods
# StandardScaler for features with large scale (net_sales, margin)
scaler_standard = StandardScaler()

# MinMaxScaler for bounded features (NPS)
scaler_minmax = MinMaxScaler()

# RobustScaler for skewed features (sales from new products)
scaler_robust = RobustScaler()

# 1) Net sales (StandardScaler)
df["net_sales_adj_norm"] = scaler_standard.fit_transform(df[["net_sales_adj"]])

# 2) Margin (StandardScaler)
df["margin_norm"] = scaler_standard.fit_transform(df[["margin_pct"]])

# 3) Product mix (simple MinMax scaling for each component)
pm_cols = ["pm_refrigerator_pct", "pm_washer_pct", "pm_oven_pct", "pm_other_pct"]
df[[col + "_norm" for col in pm_cols]] = MinMaxScaler().fit_transform(df[pm_cols])

# 4) NPS (MinMax scaling [-20, 80] → [0, 1])
df["nps_norm"] = scaler_minmax.fit_transform(df[["nps"]])

# 5) Sales from new products (RobustScaler)
df["sales_new_norm"] = scaler_robust.fit_transform(df[["sales_new_pct_of_sales"]])

# Save normalized data
out_path = os.path.join(out_dir, "normalized_kpi.csv")
df.to_csv(out_path, index=False)

print("✅ Normalized data saved to:", out_path)
print(df.head().to_string(index=False))
