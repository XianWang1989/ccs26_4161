
import datetime
import pytz

# Define the local time components
year = 2012
month = 12
day = 2
hour = 13
min = 1

# Define the local timezone
local_tz = pytz.timezone('Europe/Copenhagen')

# Create a naive datetime object (without timezone info)
naive_dt = datetime.datetime(year, month, day, hour, min)

# Localize it to the Copenhagen timezone
localized_dt = local_tz.localize(naive_dt)

# Convert to UTC
utc_dt = localized_dt.astimezone(pytz.utc)

# Display the results
print("Local time:", localized_dt)
print("UTC time:", utc_dt)
