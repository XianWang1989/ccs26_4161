
import datetime
import pytz

# Define the local timezone
local_tz = pytz.timezone('Europe/Copenhagen')

# Local time inputs
year = 2012
month = 12
day = 2
hour = 13
min = 1

# Create a naive datetime (without timezone info)
naive_datetime = datetime.datetime(year, month, day, hour, min)

# Localize the naive datetime to Europe/Copenhagen timezone
localized_datetime = local_tz.localize(naive_datetime)

# Convert localized datetime to UTC
utc_datetime = localized_datetime.astimezone(pytz.utc)

# Print results
print("Localized time:", localized_datetime)
print("UTC time:", utc_datetime)
