
import pandas as pd
import time

start_time = time.time()

# Specify the path to your CSV file
data_path = r"C:\Users\eduardo\.xy\startups\INDV14.CSV"

# Load the CSV file directly into a DataFrame
# Adjust the delimiter as necessary for your file format
df = pd.read_csv(data_path, delimiter=';', header=None)

# Extract the third column (index 2)
ticks = df[2].astype(int)  # Convert to integer

# Calculate the percentage change
daily_returns = ticks.pct_change(periods=1)

# Save the results to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

print(f"Processing time: {time.time() - start_time:.2f} seconds")
