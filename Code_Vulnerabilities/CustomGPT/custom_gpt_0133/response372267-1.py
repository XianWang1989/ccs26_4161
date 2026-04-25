
import pandas as pd
import numpy as np

# Create the DataFrame
df = pd.DataFrame({'Date': ['2014-10-20 10:44:31', '2014-10-23 09:33:46', 'nan', '2014-10-01 09:38:45']})

# Convert the 'Date' column to datetime, handling errors and nulls
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Display the DataFrame to see the results
print(df)
