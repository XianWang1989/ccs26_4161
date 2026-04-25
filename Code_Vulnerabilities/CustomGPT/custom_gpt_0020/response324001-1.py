
from datetime import datetime

# Get the current timestamp
now = datetime.now()

# Format the timestamp with microseconds
timestamp = now.strftime('%d-%m-%Y %H:%M:%S.%f')

# Round microseconds to 2 decimal places (tens of microseconds)
timestamp_rounded = timestamp[:-3] + timestamp[-3:-1]

print(timestamp_rounded)
