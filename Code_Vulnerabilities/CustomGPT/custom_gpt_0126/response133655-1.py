
import datetime
import pytz

# Define your local time components
year = 2012
month = 12
day = 2
hour = 13
minute = 1

# Create a timezone-aware datetime object in the local timezone
local_tz = pytz.timezone('Europe/Copenhagen')
local_time = local_tz.localize(datetime.datetime(year, month, day, hour, minute))

# Convert the localized time to UTC
utc_time = local_time.astimezone(pytz.utc)

# Print both local and UTC times
print("Local time:", local_time)
print("UTC time:", utc_time)
