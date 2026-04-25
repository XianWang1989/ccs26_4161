
import datetime
import pytz

# Define your local timezone
local_tz = pytz.timezone('Europe/Copenhagen')

# Create a naive datetime object (without timezone info)
naive_dt = datetime.datetime(year=2012, month=12, day=2, hour=13, minute=1)

# Localize the naive datetime to the local timezone
localized_dt = local_tz.localize(naive_dt)

# Convert the localized datetime to UTC
utc_dt = localized_dt.astimezone(pytz.utc)

# Print the results
print("Localized time in Copenhagen:", localized_dt)
print("Converted time in UTC:", utc_dt)
