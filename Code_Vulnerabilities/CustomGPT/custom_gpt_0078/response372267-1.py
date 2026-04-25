
import pandas as pd
import numpy as np

# Create the DataFrame with potential 'nan' values
df = pd.DataFrame({'Date': ['2014-10-20 10:44:31', '2014-10-23 09:33:46', 'nan', '2014-10-01 09:38:45']})

# Replace 'nan' strings with np.nan
df['Date'] = df['Date'].replace('nan', np.nan)

# Convert the 'Date' column to datetime, coercing errors to NaT
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

print(df)
