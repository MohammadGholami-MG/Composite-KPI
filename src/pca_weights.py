import pandas as pd
import numpy as np

# Read the loadings data from a CSV file
# Assumes the CSV has a column 'KPI' as the index and columns 'PC1', 'PC2', ..., 'PC8'
loadings_df = pd.read_csv('data/pca/kpi_loadings.csv', index_col=0)

# Extract the list of KPIs from the index of loadings_df
kpis = loadings_df.index.tolist()

# Calculate weights using the first 4 principal components
first_k = 4
loadings_first_k = loadings_df.iloc[:, :first_k]
communalities = (loadings_first_k ** 2).sum(axis=1)
weights = communalities / communalities.sum()

# Display the weights for each KPI
print("KPI Weights (based on communality of the first 4 PCs):")
weights_df = pd.DataFrame({'Communality': communalities, 'Weight': weights})
print(weights_df.round(4))

# Save the weights to a CSV file
weights_df.to_csv('data/weights/pca-weights/kpi_weights4.csv')