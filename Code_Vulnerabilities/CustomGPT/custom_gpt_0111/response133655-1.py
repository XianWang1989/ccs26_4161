
import datetime
import pytz

# Given local time in Copenhagen
year = 2012
month = 12
day = 2
hour = 13
minute = 1

# Create a timezone object for Europe/Copenhagen
local_tz = pytz.timezone('Europe/Copenhagen')

# Create a naive datetime object (not timezone aware)
local_time = datetime.datetime(year, month, day, hour, minute)

# Localize the naive datetime to the local timezone
localized_time = local_tz.localize(local_time)

# Convert the localized time to UTC
utc_time = localized_time.astimezone(pytz.utc)

print("Local time in Copenhagen:", localized_time)
print("Corresponding UTC time:", utc_time)
