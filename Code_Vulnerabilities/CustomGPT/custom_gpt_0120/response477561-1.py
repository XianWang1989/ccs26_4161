
import pandas as pd
from datetime import datetime

start_time = datetime.now()

# Define the path to your CSV file
data_path = r"C:\Users\eduardo\.xy\startups\INDV14.CSV"

# Load the CSV file directly using pandas
# Specify the separator based on your data format
df = pd.read_csv(data_path, sep='[; ]', engine='python', header=None)

# Extract the third column (index 2)
ticks = df[2].astype(int)

# Create a pandas DataFrame and compute pct_change
deals = pd.DataFrame(ticks)
daily_returns = deals.pct_change(periods=1)

# Save the results to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

print(f"Processing time: {datetime.now() - start_time}")
