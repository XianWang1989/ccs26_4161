
from datetime import datetime

# Current time
now = datetime.now()

# Format datetime with microseconds rounded to 2 decimal places
formatted_time = now.strftime('%d-%m-%Y %H:%M:%S') + f'.{now.microsecond // 10000:02}'
print(formatted_time)
