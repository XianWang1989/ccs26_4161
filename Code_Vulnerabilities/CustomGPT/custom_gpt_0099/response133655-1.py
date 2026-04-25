
import datetime
import pytz

# Input datetime components
year = 2012
month = 12
day = 2
hour = 13
minute = 1

# Define the local timezone
local_tz = pytz.timezone('Europe/Copenhagen')

# Create a naive datetime object (not timezone-aware)
naive_dt = datetime.datetime(year, month, day, hour, minute)

# Localize the naive datetime to the local timezone
localized_dt = local_tz.localize(naive_dt)

# Convert local time to UTC
utc_dt = localized_dt.astimezone(pytz.utc)

# Print the results
print("Local time:", localized_dt)
print("UTC time:", utc_dt)
