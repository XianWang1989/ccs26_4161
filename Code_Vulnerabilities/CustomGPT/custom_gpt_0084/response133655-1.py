
import datetime
import pytz

# Define the local timezone
local_tz = pytz.timezone('Europe/Copenhagen')

# Define the local time
year = 2012
month = 12
day = 2
hour = 13
minute = 1

# Create a naive datetime object (no timezone)
local_time = datetime.datetime(year, month, day, hour, minute)

# Localize the naive datetime to the local timezone
localized_time = local_tz.localize(local_time)

# Convert to UTC
utc_time = localized_time.astimezone(pytz.utc)

print("Local Time (Copenhagen):", localized_time)
print("Converted Time (UTC):", utc_time)
