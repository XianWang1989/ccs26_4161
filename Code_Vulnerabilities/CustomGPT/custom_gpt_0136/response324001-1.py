
from datetime import datetime

# Current timestamp
now = datetime.now()

# Convert microseconds to tens of microseconds
tens_of_microseconds = round(now.microsecond / 10000, 2)

# Format the timestamp with rounded tens of microseconds
formatted_timestamp = now.strftime(f'%d-%m-%Y %H:%M:%S.{int(tens_of_microseconds * 100)}')

print(formatted_timestamp)
