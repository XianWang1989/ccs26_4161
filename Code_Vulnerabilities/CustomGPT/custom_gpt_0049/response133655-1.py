
import datetime
import pytz

# Specify the local time details
year = 2012
month = 12
day = 2
hour = 13
minute = 1

# Create a timezone object for 'Europe/Copenhagen'
local_tz = pytz.timezone('Europe/Copenhagen')

# Create a naive datetime object for the local time
naive_local_time = datetime.datetime(year, month, day, hour, minute)

# Localize the naive datetime object to the specified timezone
localized_time = local_tz.localize(naive_local_time)

# Convert the localized time to UTC
utc_time = localized_time.astimezone(pytz.utc)

print("Localized time (Copenhagen):", localized_time)  # 2012-12-02 13:01:00+01:00
print("Converted time (UTC):", utc_time)                # Should give you 2012-12-02 12:01:00+00:00
