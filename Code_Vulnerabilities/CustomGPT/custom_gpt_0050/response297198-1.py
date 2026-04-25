
import pandas as pd

# Attempt to read the CSV with specified column types
try:
    df = pd.read_csv('leads.csv', dtype={'col11': 'str', 'col12': 'str', 'col13': 'str',
                                          'col14': 'str', 'col17': 'str', 'col19': 'str', 
                                          'col20': 'str', 'col21': 'str'})
except ValueError as e:
    print(f"ValueError: {e}")

# Check for non-Boolean values in Column K (col11)
problematic_rows = df[~df['col11'].isin(['TRUE', 'FALSE'])]
print(problematic_rows)
