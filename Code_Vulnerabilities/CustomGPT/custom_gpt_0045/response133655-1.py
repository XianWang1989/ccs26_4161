
import datetime
import pytz

# Provided local time components
year = 2012
month = 12
day = 2
hour = 13
min = 1

# Create a naive datetime object
local_dt = datetime.datetime(year, month, day, hour, min)

# Specify the local timezone
local_tz = pytz.timezone('Europe/Copenhagen')

# Localize the naive datetime object to the local timezone
localized_dt = local_tz.localize(local_dt)

# Convert the localized datetime to UTC
utc_dt = localized_dt.astimezone(pytz.utc)

# Print the result
print("Localized time:", localized_dt)  # This is the local time
print("UTC time:", utc_dt)                # This is the converted UTC time
