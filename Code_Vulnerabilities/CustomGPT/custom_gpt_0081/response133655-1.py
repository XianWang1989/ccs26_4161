
import datetime
import pytz

# Local time details
year = 2012
month = 12
day = 2
hour = 13
min = 1

# Define the local timezone and create a naive datetime object
local_tz = pytz.timezone('Europe/Copenhagen')
naive_datetime = datetime.datetime(year, month, day, hour, min)

# Localize the naive datetime to the local timezone
local_datetime = local_tz.localize(naive_datetime)

# Convert the localized time to UTC
utc_datetime = local_datetime.astimezone(pytz.utc)

print("Local time (Copenhagen):", local_datetime)
print("UTC time:", utc_datetime)
