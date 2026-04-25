
import pandas as pd
import numpy as np

# Create your DataFrame with some 'nan' strings
df = pd.DataFrame({'Date':['2014-10-20 10:44:31', '2014-10-23 09:33:46', 'nan', '2014-10-01 09:38:45']})

# Replace 'nan' string with actual np.nan
df['Date'].replace('nan', np.nan, inplace=True)

# Use pd.to_datetime to convert the Date column, handling nulls automatically
df['Date'] = pd.to_datetime(df['Date'])

print(df)
