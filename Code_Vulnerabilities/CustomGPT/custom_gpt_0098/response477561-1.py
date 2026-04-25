
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Path to the CSV file
data_path = "C:/Users/eduardo/.xy/startups/INDV14.CSV"

# Read the CSV file using pandas
# Specify the delimiter as needed
df = pd.read_csv(data_path, delimiter=';', header=None, usecols=[2])

# Calculate percentage change
daily_returns = df.pct_change(periods=1)

# Save the results to a new CSV file
daily_returns.to_csv('returns.csv', index=False, header=False)

# Output the time taken
print("Time taken:", datetime.now() - startTime)
