
import datetime
import pytz

# Define local time variables
year = 2012
month = 12
day = 2
hour = 13
min = 1

# Create a timezone object for Copenhagen
local_tz = pytz.timezone('Europe/Copenhagen')

# Create a naive datetime object (not timezone-aware)
local_dt = datetime.datetime(year, month, day, hour, min)

# Localize the naive datetime object to the Copenhagen timezone
localized_dt = local_tz.localize(local_dt)

# Convert the localized datetime object to UTC
utc_dt = localized_dt.astimezone(pytz.utc)

# Output the results
print("Local time in Copenhagen:", localized_dt)
print("Converted UTC time:", utc_dt)
