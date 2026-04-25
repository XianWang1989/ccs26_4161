
import datetime
import pytz

# Define the local time
year = 2012
month = 12
day = 2
hour = 13
minute = 1

# Define the local timezone
local_tz = pytz.timezone('Europe/Copenhagen')

# Localize the time
local_time = local_tz.localize(datetime.datetime(year, month, day, hour, minute))

# Convert to UTC
utc_time = local_time.astimezone(pytz.utc)

# Print the results
print("Local time:", local_time)
print("UTC time:", utc_time)
