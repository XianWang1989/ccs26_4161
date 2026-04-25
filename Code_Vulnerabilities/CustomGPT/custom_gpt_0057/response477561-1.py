
import pandas as pd
from datetime import datetime

start_time = datetime.now()

data_path = r"C:\Users\eduardo\.xy\startups\INDV14.CSV"

# Load CSV directly into DataFrame
df = pd.read_csv(data_path, delimiter=';', usecols=[2], header=None)

# Compute percentage change
daily_returns = df.pct_change(periods=1)

# Save to new CSV file
daily_returns.to_csv('returns.csv', index=False)

print(daily_returns)
print("Execution Time: ", datetime.now() - start_time)
