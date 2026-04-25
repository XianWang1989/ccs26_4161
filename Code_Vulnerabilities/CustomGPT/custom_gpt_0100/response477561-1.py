
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Path to your CSV file
data_path = r"C:\Users\eduardo\.xy\startups\INDV14.CSV"

# Load the CSV into a DataFrame
# Use appropriate separators while reading the CSV
df = pd.read_csv(data_path, delimiter=';', header=None)

# Extract the third column (index 2)
ticks = df[2].astype(int)  # Convert to integer type

# Compute percentage changes
daily_returns = ticks.pct_change(periods=1)

# Save the daily returns to a new CSV file
returns_path = 'returns.csv'
daily_returns.to_csv(returns_path, index=False, header=True)

print(f"Processed in: {datetime.now() - startTime}")
