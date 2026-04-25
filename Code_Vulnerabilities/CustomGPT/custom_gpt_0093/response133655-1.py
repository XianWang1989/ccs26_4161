
import datetime
import pytz

# Define the local time parameters
year = 2012
month = 12
day = 2
hour = 13
minute = 1

# Create a timezone object for Europe/Copenhagen
local_tz = pytz.timezone('Europe/Copenhagen')

# Create a naive datetime object (no timezone info)
naive_time = datetime.datetime(year, month, day, hour, minute)

# Localize the naive datetime object to the local timezone
localized_time = local_tz.localize(naive_time)

# Convert the localized time to UTC
utc_time = localized_time.astimezone(pytz.utc)

print("Localized time (Copenhagen):", localized_time)
print("Converted to UTC:", utc_time)
