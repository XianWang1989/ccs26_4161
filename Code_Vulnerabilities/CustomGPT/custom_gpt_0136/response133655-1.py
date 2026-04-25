
import datetime
import pytz

# Define the local timezone
local_tz = pytz.timezone('Europe/Copenhagen')

# Given local time components
year = 2012
month = 12
day = 2
hour = 13
minute = 1

# Create a naive datetime object (without timezone info)
local_datetime = datetime.datetime(year, month, day, hour, minute)

# Localize this naive datetime to the local timezone
localized_datetime = local_tz.localize(local_datetime)

# Convert to UTC
utc_datetime = localized_datetime.astimezone(pytz.utc)

# Print the results
print("Local datetime:", localized_datetime)
print("UTC datetime:", utc_datetime)
