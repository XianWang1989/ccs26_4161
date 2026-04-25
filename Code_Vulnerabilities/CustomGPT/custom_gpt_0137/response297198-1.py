
import pandas as pd

# Read the CSV, but do not convert dtypes yet
leads_df = pd.read_csv('leads.csv', low_memory=False)

# Check for mixed types in the problematic columns
for column in leads_df.columns:
    # Check if the column name is one of those mentioned in the warning
    if column in [11, 12, 13, 14, 17, 19, 20, 21]:  # Adjust based on actual column names
        # Identify non-boolean types for the boolean column example
        if column == 11:  # Example for column 11
            non_bool_rows = leads_df[~leads_df[column].isin(['TRUE', 'FALSE'])]
            print(f'Non-boolean values in column {column}:')
            print(non_bool_rows)

# Display potential mixed types
print(leads_df.dtypes)
