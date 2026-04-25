
from datetime import datetime

# Get the current time
now = datetime.now()

# Format the timestamp, rounding microseconds to 2 decimal places
formatted_timestamp = now.strftime('%d-%m-%Y %H:%M:%S.') + f'{int(now.microsecond / 10000):02}'

print(formatted_timestamp)
