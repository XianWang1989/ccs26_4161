
import pandas as pd

# Create a DataFrame with date strings and 'nan' strings
df = pd.DataFrame({'Date': ['2014-10-20 10:44:31', '2014-10-23 09:33:46', 'nan', '2014-10-01 09:38:45']})

# Use pd.to_datetime() to convert the Date column, allowing errors='coerce' to handle invalid parsing
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Now df['Date'] will have NaT for the 'nan' and the valid dates converted correctly
print(df)
