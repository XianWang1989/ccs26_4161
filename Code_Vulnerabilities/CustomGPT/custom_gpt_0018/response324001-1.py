
from datetime import datetime

# Get the current time
now = datetime.now()

# Format timestamp with microseconds rounded to two decimal places
formatted_timestamp = now.strftime('%d-%m-%Y %H:%M:%S.') + f'{now.microsecond // 10000:02}'  # Round down to tens of microseconds

print(formatted_timestamp)
