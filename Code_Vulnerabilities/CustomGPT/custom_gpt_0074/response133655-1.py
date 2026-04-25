
import datetime
import pytz

# Set the local time variables
year = 2012
month = 12
day = 2
hour = 13
minute = 1

# Define the local timezone
local_tz = pytz.timezone('Europe/Copenhagen')

# Create a naive datetime object (not timezone aware)
naive_dt = datetime.datetime(year, month, day, hour, minute)

# Localize the naive datetime to the local timezone
localized_dt = local_tz.localize(naive_dt)

# Convert the localized datetime to UTC
utc_dt = localized_dt.astimezone(pytz.utc)

print("Local Time:", localized_dt)
print("UTC Time:", utc_dt)
