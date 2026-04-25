
import pandas as pd

# Define a custom function to catch dtype issues
def check_dtype(value):
    if isinstance(value, str) and value.strip() not in {'TRUE', 'FALSE'}:
        raise ValueError(f"Unexpected value: {value}")
    return value

# Attempt to load the CSV and identify issues
try:
    df = pd.read_csv('leads.csv', converters={11: check_dtype})  # Adjust column index as needed
except ValueError as e:
    print(e)
