
import pandas as pd
import numpy as np

# Create DataFrame with dates and 'nan' as strings
df = pd.DataFrame({'Date': ['2014-10-20 10:44:31', '2014-10-23 09:33:46', 'nan', '2014-10-01 09:38:45']})

# Replace 'nan' strings with actual NaN values
df['Date'] = df['Date'].replace('nan', np.nan)

# Convert to datetime, automatically handling NaT for nulls
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d %H:%M:%S', errors='coerce')

print(df)
