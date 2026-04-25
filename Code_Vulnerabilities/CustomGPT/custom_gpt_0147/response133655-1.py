
import pytz
from datetime import datetime

# Define the local time in Copenhagen
year = 2012
month = 12
day = 2
hour = 13
min = 1

# Create a timezone object for Europe/Copenhagen
local_tz = pytz.timezone('Europe/Copenhagen')

# Create a naive datetime object for the local time
local_time = datetime(year, month, day, hour, min)

# Localize the naive datetime object to the local timezone
localized_time = local_tz.localize(local_time)

# Convert the localized time to UTC
utc_time = localized_time.astimezone(pytz.utc)

# Output the results
print(f"Localized Time (Copenhagen): {localized_time}")
print(f"Converted UTC Time: {utc_time}")
