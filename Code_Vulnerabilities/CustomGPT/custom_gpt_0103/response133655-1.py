
import datetime
import pytz

# Given local time components
year = 2012
month = 12
day = 2
hour = 13
min = 1

# Define the local timezone
local_tz = pytz.timezone('Europe/Copenhagen')

# Create a naive datetime object
local_time_naive = datetime.datetime(year, month, day, hour, min)

# Localize the naive datetime object toCopenhagen time
local_time = local_tz.localize(local_time_naive)

# Convert to UTC
utc_time = local_time.astimezone(pytz.utc)

# Print the results
print("Local time:", local_time)
print("UTC time:", utc_time)
