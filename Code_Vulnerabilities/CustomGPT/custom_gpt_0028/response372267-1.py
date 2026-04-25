
import pandas as pd

# Create the DataFrame with 'nan' as a string
df = pd.DataFrame({'Date': ['2014-10-20 10:44:31', '2014-10-23 09:33:46', 'nan', '2014-10-01 09:38:45']})

# Replace 'nan' strings with actual NaT (Not a Time)
df['Date'] = df['Date'].replace('nan', pd.NA)

# Convert to datetime
df['Date'] = pd.to_datetime(df['Date'])

print(df)
