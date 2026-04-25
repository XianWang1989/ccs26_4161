
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Define the path to your CSV file
data_path = "C:\\Users\\eduardo\\.xy\\startups\\INDV14.CSV"

# Read the CSV file with pandas, specifying the delimiter
df = pd.read_csv(data_path, sep=';', header=None, usecols=[2], names=['ticks'])

# Compute percentage change
daily_returns = df['ticks'].astype(float).pct_change(periods=1)

# Save the results to a new CSV file
returns_file_path = 'returns.csv'
daily_returns.to_csv(returns_file_path, header=False)

print(f"Processing time: {datetime.now() - startTime}")
