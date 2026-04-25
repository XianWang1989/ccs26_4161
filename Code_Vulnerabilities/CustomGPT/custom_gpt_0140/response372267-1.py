
import pandas as pd
import numpy as np

# Create the DataFrame
df = pd.DataFrame({'Date': ['2014-10-20 10:44:31', '2014-10-23 09:33:46', 'nan', '2014-10-01 09:38:45']})

# Replace 'nan' string with np.nan
df['Date'].replace('nan', np.nan, inplace=True)

# Convert to datetime, setting errors='coerce' to handle invalid parsing
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Display the DataFrame
print(df)
