
import pandas as pd

# Specify the data types for known columns
dtype_dict = {
    'ColumnK': 'bool',           # Assuming Column K is the 11th column
    'Column12': 'string',        # Replace with actual column names
    'Column13': 'string',
    # Add other columns as needed...
}

# Read the CSV and explicitly set dtypes
data = pd.read_csv('leads.csv', dtype=dtype_dict)

# Check the data for any remaining anomalies
print(data.info())
# Identify rows with any anomalous values
anomalies = data[data['ColumnK'].apply(lambda x: x not in [True, False])]
print(anomalies)
