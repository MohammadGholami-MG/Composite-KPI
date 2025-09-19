import pandas as pd
import numpy as np
import os
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.tools.tools import add_constant

# File paths
file_path = os.path.join("data", "dummy", "data_adjusted.csv")
out_dir = os.path.join("data", "preprocessing", "eda_results")
os.makedirs(out_dir, exist_ok=True)

# Load dataset
df = pd.read_csv(file_path, parse_dates=["date"])

# Select only KPI columns (exclude date)
kpi_cols = ["net_sales_adj", "margin_pct", "nps", 
            "sales_new_pct_of_sales", 
            "pm_refrigerator_pct", "pm_washer_pct", "pm_oven_pct", "pm_other_pct"]

df_kpi = df[kpi_cols]

# 1) Pearson Correlation
pearson_corr = df_kpi.corr(method="pearson")
pearson_path = os.path.join(out_dir, "pearson_correlation.csv")
pearson_corr.to_csv(pearson_path)
print(f"Saved Pearson correlation matrix to: {pearson_path}")

plt.figure(figsize=(10, 8))
sns.heatmap(pearson_corr, annot=True, cmap="coolwarm", center=0)
plt.title("Pearson Correlation Heatmap")
plt.tight_layout()
plt.savefig(os.path.join(out_dir, "pearson_heatmap.png"))
plt.close()

# 2) Spearman Correlation
spearman_corr = df_kpi.corr(method="spearman")
spearman_path = os.path.join(out_dir, "spearman_correlation.csv")
spearman_corr.to_csv(spearman_path)
print(f"Saved Spearman correlation matrix to: {spearman_path}")

plt.figure(figsize=(10, 8))
sns.heatmap(spearman_corr, annot=True, cmap="coolwarm", center=0)
plt.title("Spearman Correlation Heatmap")
plt.tight_layout()
plt.savefig(os.path.join(out_dir, "spearman_heatmap.png"))
plt.close()

# 3) Variance Inflation Factor (VIF)
X = add_constant(df_kpi)
vif_data = pd.DataFrame()
vif_data["Feature"] = X.columns
vif_data["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]

vif_path = os.path.join(out_dir, "vif.csv")
vif_data.to_csv(vif_path, index=False)
print(f"Saved VIF table to: {vif_path}")
