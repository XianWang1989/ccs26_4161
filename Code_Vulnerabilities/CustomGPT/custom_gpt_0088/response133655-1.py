
import pytz
from datetime import datetime

# Define your local time components
year = 2012
month = 12
day = 2
hour = 13
minute = 1

# Create a timezone object for Europe/Copenhagen
local_tz = pytz.timezone('Europe/Copenhagen')

# Create a naive datetime object (no timezone info)
naive_dt = datetime(year, month, day, hour, minute)

# Localize your naive datetime to Europe/Copenhagen
localized_dt = local_tz.localize(naive_dt)

# Convert to UTC
utc_dt = localized_dt.astimezone(pytz.utc)

# Print the results
print("Localized time:", localized_dt)
print("UTC time:", utc_dt)
