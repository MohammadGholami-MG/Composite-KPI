import os
import pandas as pd
from sklearn.decomposition import PCA

# Load normalized data
df = pd.read_csv("data/normalized/normalized_kpi.csv")

# Select only normalized columns (those ending with "_norm")
norm_cols = [col for col in df.columns if col.endswith("_norm")]

X = df[norm_cols]

# Run PCA
pca = PCA()
pca.fit(X)

# 1) Explained variance ratio for each principal component
explained_var = pca.explained_variance_ratio_
print("Explained Variance Ratio:", explained_var)
print("Cumulative Variance:", explained_var.cumsum())

# 2) Feature loadings (contribution of each feature to each PC)
loadings = pd.DataFrame(
    pca.components_.T,
    columns=[f"PC{i+1}" for i in range(len(norm_cols))],
    index=norm_cols
)
print("\nFeature Loadings:")
print(loadings)

# 3) Transformed dataset (principal component scores for each record)
df_pca = pd.DataFrame(
    pca.transform(X),
    columns=[f"PC{i+1}" for i in range(len(norm_cols))]
)
df_pca["date"] = df["date"]  # Add date column back for time-series analysis

# Create output directory if it does not exist
out_dir = os.path.join("data", "pca")
os.makedirs(out_dir, exist_ok=True)

# Save PCA results
df_pca.to_csv(os.path.join(out_dir, "kpi_pca.csv"), index=False)
loadings.to_csv(os.path.join(out_dir, "kpi_loadings.csv"))

print("\n PCA results saved to:", os.path.join(out_dir, "kpi_pca.csv"))
print(" Feature Loadings saved to:", os.path.join(out_dir, "kpi_loadings.csv"))
