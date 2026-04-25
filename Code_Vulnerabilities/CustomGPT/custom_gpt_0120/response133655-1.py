
import datetime
import pytz

# Given local time components
year = 2012
month = 12
day = 2
hour = 13
minute = 1

# Specify the local timezone
local_tz = pytz.timezone('Europe/Copenhagen')

# Create a naive datetime object (no timezone info)
local_time = datetime.datetime(year, month, day, hour, minute)

# Localize it to the 'Europe/Copenhagen' timezone
localized_time = local_tz.localize(local_time)

# Convert it to UTC
utc_time = localized_time.astimezone(pytz.utc)

# Print the results
print("Localized Time:", localized_time)
print("UTC Time:", utc_time)
