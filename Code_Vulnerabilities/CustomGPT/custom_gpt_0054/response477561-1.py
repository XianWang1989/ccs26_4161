
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Specify the path to your CSV file
data_path = "C:\\Users\\eduardo\\.xy\\startups\\INDV14.CSV"

# Read the CSV file directly into a DataFrame
# Using `sep` to define the separator based on your CSV format
# Here, it looks like the data is separated by semicolon after the space; we can read it in one go
df = pd.read_csv(data_path, sep=';', header=None, usecols=[2], names=['ticks'])

# Convert the 'ticks' column to numeric (it will handle errors if there are non-numeric values)
df['ticks'] = pd.to_numeric(df['ticks'], errors='coerce')

# Calculate the percentage change
daily_returns = df['ticks'].pct_change(periods=1)

# Output the results to a new CSV file
returns_path = "returns.csv"
daily_returns.to_csv(returns_path, index=False)

print(daily_returns)
print(f"Processing time: {datetime.now() - startTime}")
