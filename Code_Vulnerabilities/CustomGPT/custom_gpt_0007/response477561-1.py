
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Define the path to your CSV
data = "C:\\Users\\eduardo\\.xy\\startups\\INDV14.CSV"

# Read the CSV file directly into a pandas DataFrame
# Use the correct delimiter and specify the column names
df = pd.read_csv(data, delimiter=';', header=None, names=['date_time', 'volume', 'close'])

# Extract the 'close' column and convert it to a numeric type
df['close'] = pd.to_numeric(df['close'], errors='coerce')

# Now calculate the percentage change
daily_returns = df['close'].pct_change(periods=1)

# Print daily returns if needed for debugging
print(daily_returns)

# Save to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

print(f"Execution time: {datetime.now() - startTime}")
