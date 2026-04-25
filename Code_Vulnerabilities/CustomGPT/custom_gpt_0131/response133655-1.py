
import datetime
import pytz

# Define the local timezone
local_tz = pytz.timezone('Europe/Copenhagen')

# Define the local time using the provided variables
year = 2012
month = 12
day = 2
hour = 13
minute = 1

# Create a naive datetime object (without timezone information)
naive_dt = datetime.datetime(year, month, day, hour, minute)

# Localize the naive datetime to Copenhagen timezone
local_dt = local_tz.localize(naive_dt)

# Convert localized time to UTC
utc_dt = local_dt.astimezone(pytz.utc)

# Print the results
print("Local time in Copenhagen:", local_dt)
print("Converted time in UTC:", utc_dt)
