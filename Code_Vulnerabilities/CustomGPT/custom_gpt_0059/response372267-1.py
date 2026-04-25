
import pandas as pd
import numpy as np

# Create the DataFrame
df = pd.DataFrame({'Date': ['2014-10-20 10:44:31', '2014-10-23 09:33:46', 'nan', '2014-10-01 09:38:45']})

# Replace 'nan' string with actual NaN values
df['Date'].replace('nan', np.NaN, inplace=True)

# Convert the Date column to datetime
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

print(df)
