
import datetime
import pytz

# Given local time components
year = 2012
month = 12
day = 2
hour = 13
minute = 1

# Create a naive datetime object
local_naive_dt = datetime.datetime(year, month, day, hour, minute)

# Define the local timezone
local_tz = pytz.timezone('Europe/Copenhagen')

# Localize the naive datetime object to the local timezone
local_dt = local_tz.localize(local_naive_dt)

# Convert the local datetime to UTC
utc_dt = local_dt.astimezone(pytz.utc)

# Output the results
print(f"Local time in Copenhagen: {local_dt}")
print(f"UTC time: {utc_dt}")
