
import pandas as pd
from datetime import datetime

# Start time tracking
startTime = datetime.now()

# File path
data_path = "C:/Users/eduardo/.xy/startups/INDV14.CSV"

# Read the CSV file using pandas
# Specifying the delimiter. Adjust the delimiter if necessary.
df = pd.read_csv(data_path, delimiter=';', header=None)

# Extract the third column (ticks)
ticks = df[2].astype(int)  # Convert to integer

# Create DataFrame and calculate percentage change
deals = pd.DataFrame(ticks)
daily_returns = deals.pct_change(periods=1)

# Save results to a new CSV file
daily_returns.to_csv('returns.csv', index=False, header=False)

# Print elapsed time
print("Elapsed Time:", datetime.now() - startTime)
