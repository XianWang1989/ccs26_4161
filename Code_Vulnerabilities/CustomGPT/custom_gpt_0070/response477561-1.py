
import pandas as pd
from datetime import datetime

start_time = datetime.now()

# Specify the path to the CSV file
data_path = r"C:\Users\eduardo\.xy\startups\INDV14.CSV"

# Read the CSV file using pandas
# Specify the correct delimiter based on your CSV format
# Assuming `;` separates the columns
df = pd.read_csv(data_path, delimiter=';', header=None)

# Select the third column (index 2) which contains the ticks
ticks = df[2].astype(int)  # Convert to integer

# Create a DataFrame
deals = pd.DataFrame(ticks)

# Calculate percentage change
daily_returns = deals.pct_change(periods=1)

# Print daily returns
print(daily_returns)

# Save the results to a new CSV file
daily_returns.to_csv('returns.csv', index=False)

# Display the elapsed time
print("Elapsed time:", datetime.now() - start_time)
