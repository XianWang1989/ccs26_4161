
import pandas as pd

# Load CSV with coercion
data = pd.read_csv('leads.csv', low_memory=False)

# Check mixed types in specified columns
problematic_columns = data.columns[[11, 12, 13, 14, 17, 19, 20, 21]]
print(data[problematic_columns].isnull().sum())  # Show number of NaN values
