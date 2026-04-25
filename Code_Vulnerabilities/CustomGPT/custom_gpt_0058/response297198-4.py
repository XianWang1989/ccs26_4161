
import pandas as pd

# Step 1: Check unique values to identify issues
sample_df = pd.read_csv('leads.csv', nrows=100)
print("Unique values in ColumnK:", sample_df['ColumnK'].unique())

# Step 2: Read CSV explicitly setting data types
df = pd.read_csv('leads.csv', dtype={
    'ColumnK': 'bool',
    'Column12': 'str',  # Example
    # Add other columns as necessary
})

# Now, proceed with your analysis on df without the warning
