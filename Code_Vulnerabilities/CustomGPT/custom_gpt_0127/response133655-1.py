
import datetime
import pytz

# Define the local time components
year = 2012
month = 12
day = 2
hour = 13
minute = 1

# Create a naive datetime
local_time = datetime.datetime(year, month, day, hour, minute)

# Localize to 'Europe/Copenhagen'
local_tz = pytz.timezone('Europe/Copenhagen')
localized_time = local_tz.localize(local_time)

# Convert to UTC
utc_time = localized_time.astimezone(pytz.utc)

# Print the results
print("Localized time:", localized_time)
print("UTC time:", utc_time)
