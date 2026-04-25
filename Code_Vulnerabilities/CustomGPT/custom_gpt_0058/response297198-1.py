
import pandas as pd

# Read a small portion of the data to check data types
sample_df = pd.read_csv('leads.csv', nrows=100)
print(sample_df.dtypes)
