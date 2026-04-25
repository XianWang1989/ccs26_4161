
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Define the path to your CSV file
data_path = r"C:\Users\eduardo\.xy\startups\INDV14.CSV"

# Read the CSV file directly into a DataFrame, assuming the delimiter is ";"
df = pd.read_csv(data_path, delimiter=';', header=None, usecols=[2], names=['Ticks'])

# Convert the 'Ticks' column to integers (if needed)
df['Ticks'] = df['Ticks'].astype(int)

# Calculate the percentage change
daily_returns = df['Ticks'].pct_change()

# Save the results to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

print(f"Execution time: {datetime.now() - startTime}")
