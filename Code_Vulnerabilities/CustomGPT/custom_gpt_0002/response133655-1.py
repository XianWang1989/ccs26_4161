
import datetime
import pytz

# Local time parameters
year = 2012
month = 12
day = 2
hour = 13
minute = 1

# Define local timezone
local_tz = pytz.timezone('Europe/Copenhagen')

# Create a naive datetime object
naive_dt = datetime.datetime(year, month, day, hour, minute)

# Localize the naive datetime to the local timezone
local_dt = local_tz.localize(naive_dt)

# Convert to UTC
utc_dt = local_dt.astimezone(pytz.utc)

# Print the results
print("Local time in Copenhagen:", local_dt)
print("Converted to UTC:", utc_dt)
