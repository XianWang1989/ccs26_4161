
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Define the path to your CSV file
data_path = "C:\\Users\\eduardo\\.xy\\startups\\INDV14.CSV"

# Read the CSV file using pandas
# Specify the separator and only keep the third column
# Adjust the `sep` parameter depending on the actual delimiters
df = pd.read_csv(data_path, sep='[; ]+', header=None, usecols=[2])

# Compute the percentage change
daily_returns = df.pct_change(periods=1)

# Print the result
print(daily_returns)

# Save the results to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

# Print elapsed time
print("Elapsed time:", datetime.now() - startTime)
