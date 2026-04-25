
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Use pandas to read the CSV directly
data_path = r"C:\Users\eduardo\.xy\startups\INDV14.CSV"

# Read the CSV file using the appropriate delimiter
# Assuming ";" is the delimiter, you can use others as needed
df = pd.read_csv(data_path, delimiter=';', header=None, engine='c')

# Extract the third column (index 2)
# Ensure to convert to numeric in case of string types
df['ticks'] = pd.to_numeric(df[2], errors='coerce')

# Calculate percentage change
daily_returns = df['ticks'].pct_change()

# Save results to CSV
daily_returns.to_csv('returns.csv', index=False)

# Print elapsed time
print("Elapsed time:", datetime.now() - startTime)
