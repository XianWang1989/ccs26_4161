
import pandas as pd

# Step 1: Use error_bad_lines to skip problematic lines initially
leads_df = pd.read_csv('leads.csv', error_bad_lines=False)

# Optional: Identify problematic columns
for col in [11, 12, 13, 14, 17, 19, 20, 21]:  # Adjust indices for your columns
    print(f"Column {col} unique values:")
    print(leads_df.iloc[:, col].unique())

# Step 2: Specify dtype for columns during import
dtype_dict = {
    11: 'bool',  # Example for boolean column
    12: 'str',   # Example: string
    13: 'str',   # Example: string
    # Add additional columns as needed
}

leads_df = pd.read_csv('leads.csv', dtype=dtype_dict, low_memory=False)
