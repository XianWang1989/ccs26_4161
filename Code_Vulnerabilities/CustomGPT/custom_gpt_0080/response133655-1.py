
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

# Create a naive datetime object (not timezone-aware)
local_time_naive = datetime.datetime(year, month, day, hour, minute)

# Localize the naive datetime object to the local time zone
local_time = local_tz.localize(local_time_naive)

# Convert local time to UTC
utc_time = local_time.astimezone(pytz.utc)

# Print the result
print("Local time in Copenhagen:", local_time)
print("Converted time in UTC:", utc_time)
