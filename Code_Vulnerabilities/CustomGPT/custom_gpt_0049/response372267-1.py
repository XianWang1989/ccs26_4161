
import pandas as pd
import numpy as np

# Creating the DataFrame with date strings and 'nan'
df = pd.DataFrame({'Date': ['2014-10-20 10:44:31', '2014-10-23 09:33:46', 'nan', '2014-10-01 09:38:45']})

# Replacing 'nan' strings with actual NaT (Not a Time)
df['Date'] = df['Date'].replace('nan', np.nan)

# Converting the 'Date' column to datetime, coercing errors to NaT
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

print(df)
