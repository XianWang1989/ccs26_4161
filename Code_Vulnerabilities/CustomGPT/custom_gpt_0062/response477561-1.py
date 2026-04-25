
import pandas as pd
from datetime import datetime

start_time = datetime.now()

# Specify the correct path to your CSV file
data_path = "C:\\Users\\eduardo\\.xy\\startups\\INDV14.CSV"

# Read the CSV file directly into a DataFrame
# Specify the correct delimiters
df = pd.read_csv(data_path, delimiter=';', header=None, names=['timestamp', 'value', 'ticks'])

# Extract the 'ticks' column and convert it to numeric
df['ticks'] = pd.to_numeric(df['ticks'], errors='coerce')

# Calculate the pct_change
daily_returns = df['ticks'].pct_change(periods=1)

# Save the results to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

print(f"Processing time: {datetime.now() - start_time}")
