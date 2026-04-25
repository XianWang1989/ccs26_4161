
import pandas as pd
import numpy as np

# Create DataFrame with dates as strings and 'nan' as a string
df = pd.DataFrame({'Date': ['2014-10-20 10:44:31', '2014-10-23 09:33:46', 'nan', '2014-10-01 09:38:45']})

# Replace 'nan' strings with actual np.nan for correct null handling
df['Date'] = df['Date'].replace('nan', np.nan)

# Convert the Date column to datetime, coerce errors to handle any invalid parsing
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

print(df)
