
import pandas as pd
from datetime import datetime

start_time = datetime.now()

# File paths
data_path = r"C:\Users\eduardo\.xy\startups\INDV14.CSV"

# Read the CSV file directly into a DataFrame
# Specify the correct delimiter (in this case, ";") and `header` if needed
df = pd.read_csv(data_path, delimiter=';', header=None)

# Extract the third column (0-based index is 2)
ticks = df[2].astype(int)  # Convert to integer

# Create a DataFrame
deals = pd.DataFrame(ticks, columns=['Ticks'])

# Calculate percentage change
daily_returns = deals.pct_change()

# Save the result to a new CSV
daily_returns.to_csv('returns.csv', index=False)

# Print execution time
print(f"Elapsed time: {datetime.now() - start_time}")
