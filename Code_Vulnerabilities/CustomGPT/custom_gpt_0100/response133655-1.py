
import datetime
import pytz

# Define your local timezone
local_tz = pytz.timezone('Europe/Copenhagen')

# Local time components
year = 2012
month = 12
day = 2
hour = 13
minute = 1

# Create a naive datetime object (no timezone info)
local_time_naive = datetime.datetime(year, month, day, hour, minute)

# Localize the naive datetime to the Copenhagen timezone
localized_time = local_tz.localize(local_time_naive)

# Convert the localized time to UTC
utc_time = localized_time.astimezone(pytz.utc)

# Print the results
print("Localized Time:", localized_time)
print("UTC Time:", utc_time)
