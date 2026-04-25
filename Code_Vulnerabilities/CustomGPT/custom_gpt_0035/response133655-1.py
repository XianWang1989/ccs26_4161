
import datetime
import pytz

# Define the local timezone
local_tz = pytz.timezone('Europe/Copenhagen')

# Local date and time
year = 2012
month = 12
day = 2
hour = 13
minute = 1

# Create the local datetime and localize it
local_time = local_tz.localize(datetime.datetime(year, month, day, hour, minute))

# Convert to UTC
utc_time = local_time.astimezone(pytz.utc)

# Output the result
print("Local Time (Copenhagen):", local_time)
print("UTC Time:", utc_time)
