
import datetime
import pytz

# Define the local time variables
year = 2012
month = 12
day = 2
hour = 13
min = 1

# Create timezone object for Copenhagen
local_tz = pytz.timezone('Europe/Copenhagen')

# Create a naive datetime object representing the local time
local_time_naive = datetime.datetime(year, month, day, hour, min)

# Localize the naive datetime to Copenhagen time
local_time = local_tz.localize(local_time_naive)

# Convert local time to UTC
utc_time = local_time.astimezone(pytz.UTC)

# Print the results
print("Local time:", local_time)
print("UTC time:", utc_time)
