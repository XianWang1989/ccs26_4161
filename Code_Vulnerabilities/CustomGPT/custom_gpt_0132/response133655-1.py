
import datetime
import pytz

# Define the local timezone
local_tz = pytz.timezone('Europe/Copenhagen')

# Local time components
year = 2012
month = 12
day = 2
hour = 13
min = 1

# Create a naive datetime (without timezone info)
local_time = datetime.datetime(year, month, day, hour, min)

# Localize the naive datetime to the local timezone
localized_time = local_tz.localize(local_time)

# Convert to UTC
utc_time = localized_time.astimezone(pytz.utc)

print("Localized Time:", localized_time)
print("UTC Time:", utc_time)
