
import pytz
from datetime import datetime

# Set the local timezone
local_tz = pytz.timezone('Europe/Copenhagen')

# Create a naive datetime object for the local datetime
year = 2012
month = 12
day = 2
hour = 13
minute = 1
naive_local_dt = datetime(year, month, day, hour, minute)

# Localize the naive datetime to the local timezone
localized_dt = local_tz.localize(naive_local_dt)

# Convert the localized datetime to UTC
utc_dt = localized_dt.astimezone(pytz.utc)

# Print the results
print("Localized Time (Copenhagen):", localized_dt)
print("Converted Time (UTC):", utc_dt)
