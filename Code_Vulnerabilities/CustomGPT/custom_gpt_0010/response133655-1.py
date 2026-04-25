
import pytz
from datetime import datetime

# Local time details
year = 2012
month = 12
day = 2
hour = 13
min = 1

# Define the local timezone
local_tz = pytz.timezone('Europe/Copenhagen')

# Create a naive datetime object
naive_dt = datetime(year, month, day, hour, min)

# Localize the naive datetime to Copenhagen time
localized_dt = local_tz.localize(naive_dt)

# Convert the localized datetime to UTC
utc_dt = localized_dt.astimezone(pytz.utc)

# Print the results
print("Localized Copenhagen Time:", localized_dt)
print("Converted UTC Time:", utc_dt)
