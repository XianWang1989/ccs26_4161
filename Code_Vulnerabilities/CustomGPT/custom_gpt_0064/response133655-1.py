
import datetime
import pytz

# Given local time components
year = 2012
month = 12
day = 2
hour = 13
minute = 1

# Define the local timezone
local_tz = pytz.timezone('Europe/Copenhagen')

# Create a naive datetime object (without timezone info)
local_time = datetime.datetime(year, month, day, hour, minute)

# Localize the naive datetime to the specified timezone
localized_time = local_tz.localize(local_time)

# Convert localized time to UTC
utc_time = localized_time.astimezone(pytz.utc)

print("Local time:", localized_time)
print("UTC time:", utc_time)
