
from datetime import datetime

# Sample timestamp
now = datetime.now()

# Format the timestamp to string with microseconds
timestamp_with_microseconds = now.strftime('%d-%m-%Y %H:%M:%S.%f')

# Round the microseconds to 2 decimal places (i.e., to tens of microseconds)
formatted_timestamp = timestamp_with_microseconds[:-3] + '.' + timestamp_with_microseconds[-3:-1]

print(formatted_timestamp)
