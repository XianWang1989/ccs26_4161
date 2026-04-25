
import datetime
import pytz

# Define your local time
year, month, day, hour, minute = 2012, 12, 2, 13, 1

# Localize the time in 'Europe/Copenhagen'
local_tz = pytz.timezone('Europe/Copenhagen')
local_time = local_tz.localize(datetime.datetime(year, month, day, hour, minute))

# Convert the local time to UTC
utc_time = local_time.astimezone(pytz.utc)

# Print the results
print("Local Time:", local_time)
print("UTC Time:", utc_time)
