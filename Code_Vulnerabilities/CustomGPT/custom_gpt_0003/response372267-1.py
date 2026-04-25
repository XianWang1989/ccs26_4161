
import pandas as pd
import numpy as np

# Create the DataFrame with nan as a string
df = pd.DataFrame({'Date': ['2014-10-20 10:44:31', '2014-10-23 09:33:46', 'nan', '2014-10-01 09:38:45']})

# Use pandas to_datetime function to convert the 'Date' column
# This will convert 'nan' to NaT (Not a Time) automatically
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Display the DataFrame to confirm the conversion
print(df)
