
import datetime
import pytz

# Define the local time components
year = 2012
month = 12
day = 2
hour = 13
min = 1

# Define the local timezone
local_tz = pytz.timezone('Europe/Copenhagen')

# Create a naive datetime object (no timezone info)
local_time_naive = datetime.datetime(year, month, day, hour, min)

# Localize the naive datetime to the Europe/Copenhagen timezone
local_time = local_tz.localize(local_time_naive)

# Convert the localized time to UTC
utc_time = local_time.astimezone(pytz.UTC)

# Print the results
print("Local Time:", local_time)
print("UTC Time:", utc_time)
