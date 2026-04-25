
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Paths
data_path = r"C:\Users\eduardo\.xy\startups\INDV14.CSV"

# Read the CSV file using pandas
# Adjust the delimiter based on the CSV format
df = pd.read_csv(data_path, sep=';', header=None, usecols=[2])

# Rename the column for clarity
df.columns = ['Ticks']

# Convert to numeric type (in case of strings)
df['Ticks'] = pd.to_numeric(df['Ticks'], errors='coerce')

# Calculate percentage change
daily_returns = df['Ticks'].pct_change(periods=1)

# Save the results to a new CSV file
returns_path = r"C:\Users\eduardo\.xy\startups\returns.csv"
daily_returns.to_csv(returns_path, index=False, header=True)

# Output the time taken
print(f"Time taken: {datetime.now() - startTime}")
