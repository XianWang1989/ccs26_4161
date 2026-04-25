
import datetime
import pytz

# Define the local time components
year = 2012
month = 12
day = 2
hour = 13
min = 1

# Create a timezone object for Europe/Copenhagen
local_tz = pytz.timezone('Europe/Copenhagen')

# Create a naive datetime object for the local time
local_time = datetime.datetime(year, month, day, hour, min)

# Localize the naive datetime object to the local timezone
localized_time = local_tz.localize(local_time)

# Convert the localized time to UTC
utc_time = localized_time.astimezone(pytz.utc)

# Print the results
print("Local Time:", localized_time)  # This will show local time with offset
print("UTC Time:", utc_time)           # This will show the converted UTC time
