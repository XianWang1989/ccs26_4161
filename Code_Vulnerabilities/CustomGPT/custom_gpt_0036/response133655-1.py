
import datetime
import pytz

# Given local time
year = 2012
month = 12
day = 2
hour = 13
minute = 1

# Define the local timezone
local_tz = pytz.timezone('Europe/Copenhagen')

# Create a naive datetime (without timezone)
local_time_naive = datetime.datetime(year, month, day, hour, minute)

# Localize the naive datetime to the local timezone
local_time = local_tz.localize(local_time_naive)

# Convert to UTC
utc_time = local_time.astimezone(pytz.utc)

print(f"Local time in Copenhagen: {local_time}")
print(f"Equivalent UTC time: {utc_time}")
