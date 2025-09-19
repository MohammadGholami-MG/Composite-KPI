import pandas as pd

# Read data
# Sales data
df_sales = pd.read_csv("data/dummy/sample_kpi_5y_monthly.csv")  

# CPI data
df_cpi = pd.read_csv("data/dummy/cpi_synthetic.csv")  

# Assume both datasets have a "date" column with format YYYY-MM-DD
df_sales["date"] = pd.to_datetime(df_sales["date"])
df_cpi["date"] = pd.to_datetime(df_cpi["date"])

# Merge sales and CPI data
df = pd.merge(df_sales, df_cpi, on="date", how="left")

# Calculate adjustment factor
# CPI is usually given as an index (e.g., 100 = base year)
# Assume the CPI of the last month as the base
base_cpi = df["cpi"].iloc[-1]  

# Adjust net sales
df["net_sales_adj"] = df["net_sales_million_ir"] * (base_cpi / df["cpi"])

#Save the adjusted data to a new CSV file
df.to_csv("data/dummy/data_adjusted.csv", index=False, encoding="utf-8-sig")

print("Adjusted file successfully saved: data/dummy/data_adjusted.csv")
