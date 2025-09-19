import pandas as pd
import matplotlib.pyplot as plt
import os

# File paths
file_path = os.path.join("data", "dummy", "data_adjusted.csv")
out_dir = os.path.join("data", "preprocessing", "eda_results")
os.makedirs(out_dir, exist_ok=True)

# Load dataset
df = pd.read_csv(file_path, parse_dates=["date"])

# Select only numeric columns for statistics and plots
numeric_df = df.select_dtypes(include=["number"])

# Save descriptive statistics
desc_stats = numeric_df.describe().T  # Transpose for better readability
desc_stats.to_csv(os.path.join(out_dir, "descriptive_statistics.csv"))

# Plot line plots with markers for each KPI
for col in numeric_df.columns:
    plt.figure(figsize=(12, 5))
    plt.plot(df["date"], df[col], marker="o", linestyle="-")
    plt.title(f"Line Plot of {col}")
    plt.xlabel("Date")
    plt.ylabel(col)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.savefig(os.path.join(out_dir, f"lineplot_{col}.png"))
    plt.close()

print("EDA results (line plots, stats) saved in:", out_dir)