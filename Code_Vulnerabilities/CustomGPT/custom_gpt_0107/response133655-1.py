
import pytz
from datetime import datetime

# Define your local timezone
local_tz = pytz.timezone('Europe/Copenhagen')

# Create a naive datetime object (not timezone-aware)
local_time = datetime(year=2012, month=12, day=2, hour=13, minute=1)

# Localize the naive datetime to the specified timezone
localized_time = local_tz.localize(local_time)

# Convert the localized time to UTC
utc_time = localized_time.astimezone(pytz.utc)

print("Local time:", localized_time)
print("UTC time:", utc_time)
