
from datetime import datetime

# Get the current timestamp
now = datetime.now()

# Format the current time, rounding microseconds to 2 decimal places
timestamp = now.strftime('%d-%m-%Y %H:%M:%S.') + f'{int(now.microsecond / 10000):02}'

print(timestamp)
