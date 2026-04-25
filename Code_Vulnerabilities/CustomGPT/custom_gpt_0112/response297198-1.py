
import pandas as pd

# Load the CSV without the dtype specified
df = pd.read_csv('leads.csv', low_memory=False)

# Check the data types of the specific columns
mixed_type_columns = [11, 12, 13, 14, 17, 19, 20, 21]
for col in mixed_type_columns:
    print(f"Column {col} value types:\n{df.iloc[:, col].apply(type).value_counts()}")
