
import datetime
import pytz

# Define your local time parameters
year = 2012
month = 12
day = 2
hour = 13
minute = 1

# Local timezone
local_tz = pytz.timezone('Europe/Copenhagen')

# Create a naive datetime object
local_time_naive = datetime.datetime(year, month, day, hour, minute)

# Localize the naive datetime to the local timezone
local_time = local_tz.localize(local_time_naive)

# Convert to UTC
utc_time = local_time.astimezone(pytz.utc)

# Output the results
print("Local time (Copenhagen):", local_time)
print("UTC time:", utc_time)
