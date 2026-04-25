
import pytz
import datetime

# Define the local time
year = 2012
month = 12
day = 2
hour = 13
min = 1

# Define the timezone for Copenhagen
local_tz = pytz.timezone('Europe/Copenhagen')

# Create a naive datetime (without timezone)
naive_time = datetime.datetime(year, month, day, hour, min)

# Localize the naive datetime to Copenhagen time
localized_time = local_tz.localize(naive_time)

# Convert to UTC
utc_time = localized_time.astimezone(pytz.utc)

print("Localized Time:", localized_time)
print("UTC Time:", utc_time)
