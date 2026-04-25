
import datetime
import pytz

# Define the local time in Copenhagen
year = 2012
month = 12
day = 2
hour = 13
minute = 1

# Create a timezone object for Copenhagen
local_tz = pytz.timezone('Europe/Copenhagen')

# Create a naive datetime object (assumes it's in local time)
local_time = datetime.datetime(year, month, day, hour, minute)

# Localize the naive datetime to the specified timezone
localized_time = local_tz.localize(local_time)

# Convert the localized time to UTC
utc_time = localized_time.astimezone(pytz.utc)

print("Local Time in Copenhagen:", localized_time)
print("Converted UTC Time:", utc_time)
