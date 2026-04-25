
import datetime
import pytz

# Given local time in Copenhagen
year = 2012
month = 12
day = 2
hour = 13
minute = 1

# Create a naive datetime object
naive_dt = datetime.datetime(year, month, day, hour, minute)

# Define the local timezone
local_tz = pytz.timezone('Europe/Copenhagen')

# Localize the naive datetime to Copenhagen time
local_dt = local_tz.localize(naive_dt)

# Convert the localized time to UTC
utc_dt = local_dt.astimezone(pytz.utc)

# Print the results
print(f"Local time (Copenhagen): {local_dt}")
print(f"Converted UTC time: {utc_dt}")
