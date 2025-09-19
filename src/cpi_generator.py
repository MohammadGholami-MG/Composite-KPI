import numpy as np
import pandas as pd

# reproducibility
np.random.seed(42)

# parameters
periods = 60
dates = pd.date_range(start="2020-09-30", periods=periods, freq="ME")

# CPI
base = 100
monthly_trend = np.linspace(base, base * 3, periods)  # grow rate : 3x over 5 years 
seasonality = 2 * np.sin(2 * np.pi * (np.arange(periods) % 12) / 12)
noise = np.random.normal(0, 1.5, periods)

cpi = (monthly_trend + seasonality + noise).round(1)

cpi_df = pd.DataFrame({
    "date": dates,
    "cpi": cpi
})

# Save the file
cpi_df.to_csv("data/dummy/cpi_synthetic.csv", index=False)
print(cpi_df.head(12))
