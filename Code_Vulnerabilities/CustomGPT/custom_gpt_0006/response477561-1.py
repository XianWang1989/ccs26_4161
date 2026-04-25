
import pandas as pd
from datetime import datetime

start_time = datetime.now()

# Define the file path
data_file = r"C:\Users\eduardo\.xy\startups\INDV14.CSV"

# Read the CSV file, specify the delimiter, and extract the third column
# Adjust `delimiter` to match your actual file format (space or semicolon)
df = pd.read_csv(data_file, delimiter=';', usecols=[2], header=None, names=['Ticks'])

# Convert the 'Ticks' column to numeric, if necessary
df['Ticks'] = pd.to_numeric(df['Ticks'], errors='coerce')

# Calculate percentage change
daily_returns = df['Ticks'].pct_change(periods=1)

# Save to a new CSV file
daily_returns.to_csv('returns.csv', index=False, header=False)

print(f"Processing time: {datetime.now() - start_time}")
