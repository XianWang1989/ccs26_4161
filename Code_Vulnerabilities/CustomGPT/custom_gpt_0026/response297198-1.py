
import pandas as pd

# Load the CSV while capturing warnings
try:
    df = pd.read_csv('leads.csv', on_bad_lines='warn')
except Exception as e:
    print(f"Error loading CSV: {e}")

# Display data types of columns
print(df.dtypes)

# Show the first few rows
print(df.head())
