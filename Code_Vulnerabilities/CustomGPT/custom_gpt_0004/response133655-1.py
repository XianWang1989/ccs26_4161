
import datetime
import pytz

# Specify the local timezone
local_tz = pytz.timezone('Europe/Copenhagen')

# Given local time
year = 2012
month = 12
day = 2
hour = 13
minute = 1

# Create a naive datetime object in local time
local_time = datetime.datetime(year, month, day, hour, minute)

# Localize the naive datetime to the local timezone
localized_time = local_tz.localize(local_time)

# Convert to UTC
utc_time = localized_time.astimezone(pytz.utc)

# Print results
print("Localized time (Copenhagen):", localized_time)
print("Converted time (UTC):", utc_time)
