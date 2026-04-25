import pandas as pd
from datetime import datetime

start_time = datetime.now()

# Specify the path to your CSV file
file_path = r"C:\Users\eduardo\.xy\startups\INDV14.CSV"

# Read the CSV file directly with pandas
# Specify custom delimiter and header=None if there are no headers
df = pd.read_csv(file_path, sep='[ ;]', engine='python', header=None)

# Extract the third column (index 2)
deals = df[2]

# Convert to DataFrame and calculate percentage change
deals_df = pd.DataFrame(deals)
daily_returns = deals_df.pct_change()

# Save the output to a new CSV
daily_returns.to_csv("returns.csv", index=False)

print("Completed in:", datetime.now() - start_time)
