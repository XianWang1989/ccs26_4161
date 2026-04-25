
import pandas as pd

# Function to check for mixed types
def identify_mixed_types(df, columns):
    for col in columns:
        if df[col].apply(type).nunique() > 1:
            print(f"Mixed types found in column: {col}")
            print(df[col].unique())  # Show unique types found
            print(df[col][df[col].apply(type) != type(df[col][0])])  # Show problematic rows

# Attempt to read without low_memory
try:
    df = pd.read_csv('leads.csv', low_memory=False)
except pd.errors.ParserError:
    print("Parsing error occurred.")

# Identify columns with mixed types
mixed_type_columns = [11, 12, 13, 14, 17, 19, 20, 21]  # Replace with actual names if needed
identify_mixed_types(df, mixed_type_columns)
