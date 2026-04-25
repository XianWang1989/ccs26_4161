
import datetime
import pytz

# Define the local time details
year = 2012
month = 12
day = 2
hour = 13
minute = 1

# Create a timezone object for Europe/Copenhagen
local_tz = pytz.timezone('Europe/Copenhagen')

# Create a naive datetime object (without timezone info)
local_time_naive = datetime.datetime(year, month, day, hour, minute)

# Localize the naive datetime to the local timezone
local_time = local_tz.localize(local_time_naive)

# Convert to UTC
utc_time = local_time.astimezone(pytz.utc)

# Print results
print("Local time in Copenhagen:", local_time)
print("Converted to UTC:", utc_time)
