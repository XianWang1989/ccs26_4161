
import pandas as pd
from datetime import datetime

start_time = datetime.now()

# Define the file path
data_path = r"C:\Users\eduardo\.xy\startups\INDV14.CSV"

# Read the CSV file using pandas
# Specify the delimiter
df = pd.read_csv(data_path, sep='[ ;]', header=None, engine='python')

# Extract the third column (index 2)
ticks = df[2].astype(int)

# Create a DataFrame from the ticks
deals = pd.DataFrame(ticks)

# Calculate percentage change
daily_returns = deals.pct_change()

# Save to a new CSV file
returns_path = r'C:\Users\eduardo\.xy\returns.csv'
daily_returns.to_csv(returns_path, index=False, header=False)

# Print elapsed time
print(f"Processing time: {datetime.now() - start_time}")
