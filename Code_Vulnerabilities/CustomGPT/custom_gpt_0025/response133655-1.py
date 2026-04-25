
from datetime import datetime
import pytz

# Local time details
year = 2012
month = 12
day = 2
hour = 13
minute = 1

# Define the local timezone
local_tz = pytz.timezone('Europe/Copenhagen')

# Create a naive datetime object (not timezone-aware)
naive_time = datetime(year, month, day, hour, minute)

# Localize the naive datetime to the specified timezone
localized_time = local_tz.localize(naive_time)

# Convert to UTC
utc_time = localized_time.astimezone(pytz.utc)

print("Localized Time: ", localized_time)  # Local time with timezone info
print("UTC Time: ", utc_time)                # Converted UTC time
