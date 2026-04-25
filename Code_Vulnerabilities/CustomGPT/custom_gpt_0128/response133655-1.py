
import datetime
import pytz

# Define local time components
year = 2012
month = 12
day = 2
hour = 13
min = 1

# Create a timezone object for Europe/Copenhagen
local_tz = pytz.timezone('Europe/Copenhagen')

# Create a naive datetime object in local time
local_time_naive = datetime.datetime(year, month, day, hour, min)

# Localize the naive datetime to the Copenhagen timezone
local_time = local_tz.localize(local_time_naive)

# Convert the localized time to UTC
utc_time = local_time.astimezone(pytz.utc)

# Print the local time and the corresponding UTC time
print("Local time:", local_time)
print("UTC time:", utc_time)
