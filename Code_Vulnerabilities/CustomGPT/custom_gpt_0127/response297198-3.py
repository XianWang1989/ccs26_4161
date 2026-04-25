
import pandas as pd

# Load CSV to identify problematic types
df = pd.read_csv('leads.csv', low_memory=True)

# Check data types
print(df.dtypes)

# Check for mixed types in specific columns
problematic_columns = [11, 12, 13, 14, 17, 19, 20, 21]
for col in problematic_columns:
    mixed_type_rows = df[df.iloc[:, col].apply(type) != df.iloc[:, col].dtype.type]
    print(f"Mixed type rows in column {col}:")
    print(mixed_type_rows)

# At this point, you can decide to specify dtypes or proceed as necessary
dtype_dict = {
    'ColumnK': 'bool',   # Replace 'ColumnK' with the actual column name
    # Add other columns with their respective types
}
df_corrected = pd.read_csv('leads.csv', dtype=dtype_dict, low_memory=False)
