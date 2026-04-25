
import datetime
import pytz

# Define your local time data
year = 2012
month = 12
day = 2
hour = 13
minute = 1

# Create a timezone for Copenhagen
local_tz = pytz.timezone('Europe/Copenhagen')

# Create a naive datetime object
local_time = datetime.datetime(year, month, day, hour, minute)

# Localize the naive datetime object to Copenhagen time
localized_time = local_tz.localize(local_time)

# Convert the localized time to UTC
utc_time = localized_time.astimezone(pytz.utc)

print("Local time in Copenhagen:", localized_time)
print("Converted UTC time:", utc_time)
