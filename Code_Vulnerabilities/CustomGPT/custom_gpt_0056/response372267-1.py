
import pandas as pd
import numpy as np

# Create the DataFrame with mixed date strings and 'nan'
df = pd.DataFrame({'Date': ['2014-10-20 10:44:31', '2014-10-23 09:33:46', 'nan', '2014-10-01 09:38:45']})

# Replace 'nan' string with actual NaN values
df['Date'].replace('nan', np.NaN, inplace=True)

# Convert strings to datetime, automatically handles NaN
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d %H:%M:%S', errors='coerce')

# Display the result
print(df)
