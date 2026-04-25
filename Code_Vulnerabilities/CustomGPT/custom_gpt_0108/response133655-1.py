
import datetime
import pytz

# Local timezone
local_tz = pytz.timezone('Europe/Copenhagen')

# Given local time (year, month, day, hour, minute)
year = 2012
month = 12
day = 2
hour = 13
min = 1

# Create a naive datetime object
local_time_naive = datetime.datetime(year, month, day, hour, min)

# Localize the naive datetime to the local timezone
local_time = local_tz.localize(local_time_naive)

# Convert to UTC
utc_time = local_time.astimezone(pytz.utc)

# Print results
print("Local Time:", local_time)
print("UTC Time:", utc_time)
