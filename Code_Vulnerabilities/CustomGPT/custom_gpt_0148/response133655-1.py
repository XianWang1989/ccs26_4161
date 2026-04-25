
import datetime
import pytz

# Define the local timezone
local_tz = pytz.timezone('Europe/Copenhagen')

# Create a naive datetime object from the local time
local_time = datetime.datetime(year=2012, month=12, day=2, hour=13, minute=1)

# Localize the naive datetime object to the local timezone
localized_time = local_tz.localize(local_time)

# Convert to UTC
utc_time = localized_time.astimezone(pytz.utc)

# Print the results
print("Local Time in Copenhagen:", localized_time)
print("UTC Time:", utc_time)
