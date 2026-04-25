
import pandas as pd

# Start time measurement
start_time = pd.to_datetime('now')

# Define the file path
data = "C:\\Users\\eduardo\\.xy\\startups\\INDV14.CSV"

# Read the CSV file directly into a DataFrame
# Specify the delimiter and column names
df = pd.read_csv(data, delimiter=';', header=None, usecols=[2])

# Rename the column for convenience
df.columns = ['close']

# Convert the 'close' column to numeric in case there are any non-numeric values
df['close'] = pd.to_numeric(df['close'], errors='coerce')

# Calculate percentage change
daily_returns = df['close'].pct_change(periods=1)

# Print results
print(daily_returns)

# Save the results to a new CSV file
daily_returns.to_csv('returns.csv', index=False, header=False)

# Print the time taken for processing
print("Time taken:", pd.to_datetime('now') - start_time)
