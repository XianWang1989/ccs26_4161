
import pandas as pd
import numpy as np

# Create DataFrame with some datetime strings and 'nan'
df = pd.DataFrame({'Date': ['2014-10-20 10:44:31', '2014-10-23 09:33:46', 'nan', '2014-10-01 09:38:45']})

# Replace 'nan' string with np.NaN
df.replace('nan', np.NaN, inplace=True)

# Convert the 'Date' column to datetime, handling the NaN values
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Display the updated DataFrame
print(df)
