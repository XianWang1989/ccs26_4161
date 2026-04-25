
from datetime import datetime

# Current timestamp
now = datetime.now()

# Get the full timestamp string with microseconds
timestamp = now.strftime('%d-%m-%Y %H:%M:%S.%f')

# Round microseconds to two decimal places
microseconds = now.microsecond // 10000  # Convert microseconds to tens of microseconds
formatted_timestamp = now.strftime(f'%d-%m-%Y %H:%M:%S.{microseconds:02}')

print(formatted_timestamp)
