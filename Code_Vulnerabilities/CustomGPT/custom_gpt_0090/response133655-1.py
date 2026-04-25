
import datetime
import pytz

# Input local time details
year = 2012
month = 12
day = 2
hour = 13
minute = 1

# Define the local timezone
local_tz = pytz.timezone('Europe/Copenhagen')

# Create a naive datetime object (not aware of timezone)
local_time = datetime.datetime(year, month, day, hour, minute)

# Localize the naive datetime object to the local timezone
localized_time = local_tz.localize(local_time)

# Convert to UTC
utc_time = localized_time.astimezone(pytz.utc)

print("Local time:", localized_time)
print("UTC time:", utc_time)
