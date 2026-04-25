
from datetime import datetime

# Current time
now = datetime.now()

# Format the timestamp with microseconds rounded to two decimal places (in tens of microseconds)
formatted_time = now.strftime('%d-%m-%Y %H:%M:%S.') + f'{now.microsecond // 10000:02}'
print(formatted_time)
