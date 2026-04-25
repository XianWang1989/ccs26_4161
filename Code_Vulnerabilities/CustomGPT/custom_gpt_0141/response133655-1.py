
import datetime
import pytz

# Input your local time
year = 2012
month = 12
day = 2
hour = 13
minute = 1

# Define the local timezone
local_tz = pytz.timezone('Europe/Copenhagen')

# Create a naive datetime object
local_time = datetime.datetime(year, month, day, hour, minute)

# Localize the naive datetime to the local timezone
localized_time = local_tz.localize(local_time)

# Convert the localized time to UTC
utc_time = localized_time.astimezone(pytz.utc)

# Print the results
print("Localized time (Copenhagen):", localized_time)
print("Converted time (UTC):", utc_time)
