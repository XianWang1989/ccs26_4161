
import datetime
import pytz

# Define your local time values
year = 2012
month = 12
day = 2
hour = 13
min = 1

# Define the local timezone
local_tz = pytz.timezone('Europe/Copenhagen')

# Create a naive datetime object
naive_datetime = datetime.datetime(year, month, day, hour, min)

# Localize the naive datetime to the local timezone
localized_datetime = local_tz.localize(naive_datetime)

# Convert the localized datetime to UTC
utc_datetime = localized_datetime.astimezone(pytz.utc)

# Print the results
print("Localized datetime:", localized_datetime)
print("UTC datetime:", utc_datetime)
