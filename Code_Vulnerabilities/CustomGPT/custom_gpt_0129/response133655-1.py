
import datetime
import pytz

# Given local time in Copenhagen
year = 2012
month = 12
day = 2
hour = 13
minute = 1

# Create a timezone object for 'Europe/Copenhagen'
local_tz = pytz.timezone('Europe/Copenhagen')

# Create a naive datetime object (not timezone-aware)
local_dt = datetime.datetime(year, month, day, hour, minute)

# Localize the naive datetime object to the Copenhagen timezone
localized_dt = local_tz.localize(local_dt)

# Convert to UTC
utc_dt = localized_dt.astimezone(pytz.utc)

# Print the results
print("Localized datetime in Copenhagen:", localized_dt)
print("Converted datetime in UTC:", utc_dt)
