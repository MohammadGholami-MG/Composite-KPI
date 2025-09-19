import numpy as np
import pandas as pd
import os

# reproducibility
np.random.seed(42)

# parameters
periods = 60
dates = pd.date_range(start="2020-09-30", periods=periods, freq="ME")

# 1) Net Sales
trend = np.linspace(300_000, 750_000, periods)
seasonality = 40_000 * np.sin(2 * np.pi * (np.arange(periods) % 12) / 12)
noise = np.random.normal(0, 25_000, periods)
shocks = np.zeros(periods)
shocks[[8, 22, 35, 47]] = [-60_000, 80_000, -40_000, 100_000]
net_sales = (trend + seasonality + noise + shocks).round().astype(int)
net_sales = np.maximum(net_sales, 50_000)

# 2) Margin (%)
base_margin = 22 + 6 * np.sin(2 * np.pi * (np.arange(periods) % 24) / 24)
sales_corr = (net_sales - net_sales.mean()) / net_sales.mean() * 2
margin = (base_margin + sales_corr + np.random.normal(0, 1.2, periods)).clip(10, 45)

# 3) Product Mix
product_shares = []
for t in range(periods):
    seasonal = np.array([
        0.02 * np.sin(2 * np.pi * t / 12),
        0.01 * np.cos(2 * np.pi * t / 12),
        0.01 * np.sin(2 * np.pi * t / 6),
        -0.03 * np.sin(2 * np.pi * t / 12)
    ])
    drift = np.array([
        0.001 * (t/periods),
        -0.0005 * (t/periods),
        0.0002 * (t/periods),
        -0.0007 * (t/periods)
    ])
    noise_pm = np.random.normal(0, 0.008, 4)
    share = np.array([0.38, 0.28, 0.18, 0.16]) + seasonal + drift + noise_pm

    if t in [12, 13, 14]:
        share[0] += 0.06
        share[3] -= 0.03
    if t in [30, 31]:
        share[1] += 0.05
        share[2] -= 0.02

    share = np.clip(share, 0.02, None)
    share = share / share.sum()
    product_shares.append(share * 100)

product_shares = np.array(product_shares)
pm_cols = ["pm_refrigerator_pct", "pm_washer_pct", "pm_oven_pct", "pm_other_pct"]

# 4) NPS
nps_base = 20 + 0.00005 * (net_sales - net_sales.mean())
nps = (nps_base + 8 * np.sin(2 * np.pi * (np.arange(periods) % 12) / 12) +
       np.random.normal(0, 4, periods))
launch_months = [10, 25, 42]
for lm in launch_months:
    if lm < periods:
        nps[lm:lm+3] += 6
nps = np.clip(nps, -20, 80)

# 5) Sales from New Products
sales_new_pct = np.random.uniform(0.5, 6.0, periods)
for lm in launch_months:
    if lm < periods:
        span = min(6, periods - lm)
        sales_new_pct[lm:lm+span] += np.linspace(3, 0.5, span)
sales_new_pct = np.clip(sales_new_pct, 0, 20)

# Assemble DataFrame
df = pd.DataFrame({
    "date": dates,
    "net_sales_million_ir": net_sales,
    "margin_pct": margin,
    "nps": nps,
    "sales_new_pct_of_sales": sales_new_pct
})

for i, col in enumerate(pm_cols):
    df[col] = product_shares[:, i]

df = df.round(2)

# check
assert np.allclose(df[pm_cols].sum(axis=1), 100, atol=0.1), "Product mix rows must sum ~100"

# save
out_dir = "data"
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, "sample_kpi_5y_monthly.csv")
df.to_csv(out_path, index=False)

print("Saved sample file to:", out_path)
print(df.head().to_string(index=False))
