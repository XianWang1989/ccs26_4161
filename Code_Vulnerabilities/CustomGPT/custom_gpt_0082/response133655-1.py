
import datetime
import pytz

# Define the local timezone
local_tz = pytz.timezone('Europe/Copenhagen')

# Define the local time as naive datetime
year = 2012
month = 12
day = 2
hour = 13
min = 1

# Localize the naive datetime
local_time = datetime.datetime(year, month, day, hour, min)
localized_time = local_tz.localize(local_time)

# Convert to UTC
utc_time = localized_time.astimezone(pytz.utc)

# Output the results
print("Localized Time:", localized_time)
print("UTC Time:", utc_time)
