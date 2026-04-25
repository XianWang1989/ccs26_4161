
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Define the file path
data_path = r"C:\Users\eduardo\.xy\startups\INDV14.CSV"

# Load the data directly into a DataFrame
# Assuming your data is separated by ';' (as indicated by your CSV example)
df = pd.read_csv(data_path, sep=';', header=None, usecols=[2])

# Rename the column for easier access
df.columns = ['ticks']

# Calculate daily returns using pct_change
daily_returns = df['ticks'].pct_change()

# Print the daily returns
print(daily_returns)

# Save the returns to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

print(f"Elapsed time: {datetime.now() - startTime}")
