
import datetime
import pytz

# Define the local timezone
local_tz = pytz.timezone('Europe/Copenhagen')

# Create a naive datetime object (not timezone-aware)
naive_dt = datetime.datetime(year=2012, month=12, day=2, hour=13, minute=1)

# Localize the naive datetime to make it timezone-aware
localized_dt = local_tz.localize(naive_dt)

# Convert the localized datetime to UTC
utc_dt = localized_dt.astimezone(pytz.utc)

# Print the results
print("Local time:", localized_dt)
print("UTC time:", utc_dt)
