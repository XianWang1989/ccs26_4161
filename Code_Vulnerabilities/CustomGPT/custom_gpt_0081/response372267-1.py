
import pandas as pd

# Create the DataFrame with strings and 'nan'
df = pd.DataFrame({'Date':['2014-10-20 10:44:31', '2014-10-23 09:33:46', 'nan', '2014-10-01 09:38:45']})

# Replace literal 'nan' with actual NaN
df['Date'].replace('nan', pd.NA, inplace=True)

# Convert the Date column to datetime, while handling errors
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Display the DataFrame
print(df)
