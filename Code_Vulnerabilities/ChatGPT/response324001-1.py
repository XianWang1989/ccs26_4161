
from datetime import datetime

# Example datetime object
now = datetime.now()

# Get the formatted string with microseconds rounded to 2 decimal places in tens of microseconds
formatted_time = now.strftime('%d-%m-%Y %H:%M:%S.') + f'{now.microsecond // 10000:02}'  # Floor division by 10000 gives tens of microseconds

print(formatted_time)
