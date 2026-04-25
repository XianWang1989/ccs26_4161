
from datetime import datetime

# Get current time
now = datetime.now()

# Get the timestamp with rounded microseconds to 2 decimal places.
tens_of_microseconds = now.microsecond / 10000  # Convert to tens of microseconds
timestamp = now.strftime(f'%d-%m-%Y %H:%M:%S.{tens_of_microseconds:.2f}')

print(timestamp)
