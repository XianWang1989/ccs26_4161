
import pandas as pd
import numpy as np

# Create the DataFrame
df = pd.DataFrame({'Date': ['2014-10-20 10:44:31', '2014-10-23 09:33:46', 'nan', '2014-10-01 09:38:45']})

# Replace 'nan' string with np.nan to create actual nulls
df['Date'] = df['Date'].replace('nan', np.nan)

# Convert the Date column to datetime, handling NaT automatically
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')  # 'errors=coerce' will convert invalid parsing to NaT

# Display the DataFrame
print(df)
