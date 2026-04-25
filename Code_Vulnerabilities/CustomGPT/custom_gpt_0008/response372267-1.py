
import pandas as pd
import numpy as np

# Create the DataFrame with date strings and 'nan' as a string
df = pd.DataFrame({'Date': ['2014-10-20 10:44:31', '2014-10-23 09:33:46', 'nan', '2014-10-01 09:38:45']})

# Replace 'nan' string with actual NaN (NaT)
df['Date'] = df['Date'].replace('nan', np.nan)

# Convert the 'Date' column to datetime, handling errors
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d %H:%M:%S', errors='coerce')

print(df)
