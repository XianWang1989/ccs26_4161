
import datetime
import pytz

# Define the local timezone
local_tz = pytz.timezone('Europe/Copenhagen')

# Define the local time
year = 2012
month = 12
day = 2
hour = 13
minute = 1

# Create a naive datetime object (no timezone info)
local_time = datetime.datetime(year, month, day, hour, minute)

# Localize the naive datetime to the Copenhagen timezone
localized_time = local_tz.localize(local_time)

# Convert localized time to UTC
utc_time = localized_time.astimezone(pytz.UTC)

# Print results
print("Local time:", localized_time)  # This will show the local time
print("UTC time:", utc_time)           # This will show the UTC equivalent
