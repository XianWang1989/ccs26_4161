
from datetime import datetime

# Get the current timestamp
now = datetime.now()

# Format the timestamp, rounding microseconds to 2 decimal places (i.e., tens of microseconds)
formatted_timestamp = now.strftime('%d-%m-%Y %H:%M:%S.') + f'{int(now.microsecond / 10000):02}'

print(formatted_timestamp)
