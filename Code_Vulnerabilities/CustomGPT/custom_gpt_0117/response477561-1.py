
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Define the path to your CSV file
data_path = "C:\\Users\\eduardo\\.xy\\startups\\INDV14.CSV"

# Read the CSV file directly using pandas
# Specify the delimiter based on your data format
df = pd.read_csv(data_path, delimiter=';', header=None)

# Extract the third column (index 2) and convert it to numeric
ticks = pd.to_numeric(df[2], errors='coerce')

# Create the DataFrame and calculate pct_change
deals = pd.DataFrame(ticks)
daily_returns = deals.pct_change()

# Print or save the daily returns
print(daily_returns)

# Save to CSV
daily_returns.to_csv('returns.csv', index=False)

# Duration
print(f"Duration: {datetime.now() - startTime}")
