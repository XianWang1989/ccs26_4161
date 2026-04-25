
from datetime import datetime

# Get the current time
now = datetime.now()

# Format timestamp with microseconds rounded to 2 decimal places (tens of microseconds)
formatted_time = now.strftime('%d-%m-%Y %H:%M:%S.') + f'{now.microsecond // 10000:02}'

print(formatted_time)
