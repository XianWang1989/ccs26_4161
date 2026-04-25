
import datetime
import pytz

# Given local time components
year = 2012
month = 12
day = 2
hour = 13
minute = 1

# Specify the timezone for Europe/Copenhagen
local_tz = pytz.timezone('Europe/Copenhagen')

# Create a naive datetime object (without timezone info)
naive_dt = datetime.datetime(year, month, day, hour, minute)

# Localize this naive datetime to the 'Europe/Copenhagen' timezone
local_dt = local_tz.localize(naive_dt)

# Convert the local datetime to UTC
utc_dt = local_dt.astimezone(pytz.utc)

# Print the resulting UTC datetime
print("Local time in Copenhagen:", local_dt)
print("Converted UTC time:", utc_dt)
