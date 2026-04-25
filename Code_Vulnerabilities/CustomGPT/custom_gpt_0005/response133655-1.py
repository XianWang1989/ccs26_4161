
import datetime
import pytz

# Given local time in Copenhagen
year = 2012
month = 12
day = 2
hour = 13
min = 1

# Define the Copenhagen timezone
local_tz = pytz.timezone('Europe/Copenhagen')

# Create a naive datetime object (without timezone info)
local_time = datetime.datetime(year, month, day, hour, min)

# Localize the naive datetime to Copenhagen time
localized_time = local_tz.localize(local_time)

# Convert to UTC
utc_time = localized_time.astimezone(pytz.utc)

# Print the result
print("Localized time:", localized_time)
print("UTC time:", utc_time)
