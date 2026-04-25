
import pandas as pd
import numpy as np

# Creating a DataFrame with dates and 'nan' as a string
df = pd.DataFrame({'Date': ['2014-10-20 10:44:31', '2014-10-23 09:33:46', 'nan', '2014-10-01 09:38:45']})

# Replacing the string 'nan' with numpy's NaN value
df['Date'].replace('nan', np.nan, inplace=True)

# Converting the date strings to datetime objects, while handling NaN values
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d %H:%M:%S', errors='coerce')

# Display the DataFrame
print(df)
