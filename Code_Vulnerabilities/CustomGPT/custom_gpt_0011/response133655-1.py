
import datetime
import pytz

# Define the local time parameters
year = 2012
month = 12
day = 2
hour = 13
min = 1

# Specify the local timezone
local_tz = pytz.timezone('Europe/Copenhagen')

# Create a naive datetime object
local_time = datetime.datetime(year, month, day, hour, min)

# Localize the naive datetime to the local timezone
localized_time = local_tz.localize(local_time)

# Convert to UTC
utc_time = localized_time.astimezone(pytz.utc)

# Output the results
print("Local Time:", localized_time)
print("UTC Time:", utc_time)
