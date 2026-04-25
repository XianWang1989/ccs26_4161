
from datetime import datetime

# Get the current time
now = datetime.now()

# Convert microseconds to tens of microseconds
tens_of_microseconds = now.microsecond // 10000  # Integer division to get the value in tens of microseconds

# Formatting the timestamp
formatted_time = now.strftime('%d-%m-%Y %H:%M:%S.') + f'{tens_of_microseconds:02}'
print(formatted_time)
