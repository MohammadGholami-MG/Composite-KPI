import pandas as pd

# 1. Load the data
df_kpi = pd.read_csv("data/standardization/kpi_minmax_scaled.csv")  
df_weights = pd.read_csv("data/weights/final-weights.csv")  

# 2. Prepare the data
weights = dict(zip(df_weights["kpi"], df_weights["weights"]))
df_kpi = df_kpi[["date"] + list(weights.keys())]

# 3. Calculate the raw composite index (weighted)
for col, w in weights.items():
    df_kpi[col] = df_kpi[col] * w

df_kpi["composite_index_raw"] = df_kpi[list(weights.keys())].sum(axis=1)

# 4. Set the base index (choose method)
def apply_base_index(df, method="first", year=None):
    """
    method:
        - "first": first month = 100
        - "mean": overall average = 100
        - "year": a specific year = 100 (must specify 'year', e.g. 2020)
    """
    if method == "first":
        base_value = df.loc[0, "composite_index_raw"]

    elif method == "mean":
        base_value = df["composite_index_raw"].mean()

    elif method == "year":
        if year is None:
            raise ValueError("For 'year' method, a year must be specified")
        df["year"] = pd.to_datetime(df["date"]).dt.year
        base_value = df.loc[df["year"] == year, "composite_index_raw"].mean()

    else:
        raise ValueError("Unknown method. Only 'first', 'mean', 'year' are valid.")

    df["composite_index"] = (df["composite_index_raw"] / base_value) * 100
    return df

# 5. Apply the desired method
# Example: first month = 100
df_result = apply_base_index(df_kpi.copy(), method="first")

# Example: overall average = 100
# df_result = apply_base_index(df_kpi.copy(), method="mean")

# Example: year 2021 = 100
# df_result = apply_base_index(df_kpi.copy(), method="year", year=2021)

# 6. Save the output
df_result.to_csv("data/output/composite_index_output.csv", index=False)

print(df_result[["date", "composite_index"]].head(12))
