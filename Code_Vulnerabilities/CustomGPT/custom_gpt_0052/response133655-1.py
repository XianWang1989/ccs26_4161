
import datetime
import pytz

# Given local time info
year = 2012
month = 12
day = 2
hour = 13
minute = 1

# Define the local timezone
local_tz = pytz.timezone('Europe/Copenhagen')

# Create a naive datetime (without timezone info)
local_time_naive = datetime.datetime(year, month, day, hour, minute)

# Localize to the given timezone
localized_time = local_tz.localize(local_time_naive)

# Convert localized time to UTC
utc_time = localized_time.astimezone(pytz.utc)

# Print the results
print("Localized time (Copenhagen):", localized_time)
print("Converted time in UTC:", utc_time)
