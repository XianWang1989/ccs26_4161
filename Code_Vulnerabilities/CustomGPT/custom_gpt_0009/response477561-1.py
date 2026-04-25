
import pandas as pd
from datetime import datetime

startTime = datetime.now()

# Use pandas to read the CSV directly
data_path = "C:\\Users\\eduardo\\.xy\\startups\\INDV14.CSV"
# Specify the delimiter and read the CSV
df = pd.read_csv(data_path, delimiter=';', header=None)

# Extract the third column (index 2)
ticks = df[2].astype(int)  # Ensuring the ticks are integers

# Creating the DataFrame and calculating pct_change
deals = pd.DataFrame(ticks)
daily_returns = deals.pct_change(periods=1)

# Saving to CSV
daily_returns.to_csv('returns.csv', index=False)

print(daily_returns)
print(f"Processing Time: {datetime.now() - startTime}")
