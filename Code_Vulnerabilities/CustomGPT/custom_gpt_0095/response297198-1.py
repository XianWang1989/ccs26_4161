
import pandas as pd

# Load the data with the default settings
df = pd.read_csv('leads.csv', low_memory=True)

# Inspect the problematic columns
for col in df.columns[11:22]:  # Adjust indices for your specific case
    # Check for the types in the column
    types = df[col].apply(type).value_counts()
    print(f"Column: {col}, Type counts:\n{types}\n")

    # Display rows with mixed types
    mixed_type_rows = df[df[col].apply(type) != types.index[0]]
    print(f"Rows with mixed types in {col}:\n{mixed_type_rows}\n")
