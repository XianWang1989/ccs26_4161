
import pandas as pd
from datetime import datetime

startTime = datetime.now()

data_path = "C:/Users/eduardo/.xy/startups/INDV14.CSV"

# Read the CSV using Pandas, specifying the delimiter
df = pd.read_csv(data_path, delimiter=';', usecols=[2], header=None)

# Convert the column to numeric, errors='coerce' will replace non-convertible values with NaN
df[0] = pd.to_numeric(df[0], errors='coerce')

# Calculate percentage change
daily_returns = df.pct_change()

# Save the result to a new CSV
daily_returns.to_csv('returns.csv', index=False, header=False)

print(datetime.now() - startTime)  # Print elapsed time
