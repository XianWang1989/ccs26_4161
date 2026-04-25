
import datetime
import pytz

# Define the local time
year = 2012
month = 12
day = 2
hour = 13
min = 1

# Create the timezone object for Copenhagen
local_tz = pytz.timezone('Europe/Copenhagen')

# Create a naive datetime object for the provided local time
local_dt = datetime.datetime(year, month, day, hour, min)

# Localize the naive datetime to the Copenhagen timezone
localized_dt = local_tz.localize(local_dt)

# Convert the localized datetime to UTC
utc_dt = localized_dt.astimezone(pytz.utc)

print("Local time (Copenhagen):", localized_dt)
print("UTC time:", utc_dt)
