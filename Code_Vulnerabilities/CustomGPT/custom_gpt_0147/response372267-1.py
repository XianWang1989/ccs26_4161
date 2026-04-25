
import pandas as pd
import numpy as np

# Step 2: Create the DataFrame
df = pd.DataFrame({'Date': ['2014-10-20 10:44:31', '2014-10-23 09:33:46', 'nan', '2014-10-01 09:38:45']})

# Step 3: Replace 'nan' string with actual NaN value
df['Date'].replace('nan', np.nan, inplace=True)

# Step 4: Convert to datetime
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

print(df)
