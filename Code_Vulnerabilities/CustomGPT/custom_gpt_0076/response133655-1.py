
import datetime
import pytz

# Given local time in Europe/Copenhagen
year = 2012
month = 12
day = 2
hour = 13
minute = 1

# Create a naive datetime object
local_time = datetime.datetime(year, month, day, hour, minute)

# Localize to Europe/Copenhagen timezone
local_tz = pytz.timezone('Europe/Copenhagen')
localized_time = local_tz.localize(local_time)

# Convert to UTC
utc_time = localized_time.astimezone(pytz.utc)

# Print results
print("Localized Time:", localized_time)  # Prints: 2012-12-02 13:01:00+01:00
print("UTC Time:", utc_time)  # Should match the database entry
