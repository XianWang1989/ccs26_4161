
import pytz
from datetime import datetime

# Given local time information
year = 2012
month = 12
day = 2
hour = 13
minute = 1

# Define the local timezone
local_tz = pytz.timezone('Europe/Copenhagen')

# Create a naive datetime (without timezone info)
naive_dt = datetime(year, month, day, hour, minute)

# Localize the naive datetime to the local timezone
local_dt = local_tz.localize(naive_dt)

# Convert the localized datetime to UTC
utc_dt = local_dt.astimezone(pytz.utc)

# Print the results
print("Local Time:", local_dt)
print("UTC Time:", utc_dt)
