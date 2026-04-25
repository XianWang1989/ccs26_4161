
import datetime
import pytz

# Define the local time parameters
year = 2012
month = 12
day = 2
hour = 13
minute = 1

# Create a naive datetime object
local_time = datetime.datetime(year, month, day, hour, minute)

# Localize to the specified timezone
local_tz = pytz.timezone('Europe/Copenhagen')
localized_time = local_tz.localize(local_time)

# Convert to UTC
utc_time = localized_time.astimezone(pytz.utc)

# Display the results
print("Local Time (Copenhagen):", localized_time)
print("UTC Time:", utc_time)
