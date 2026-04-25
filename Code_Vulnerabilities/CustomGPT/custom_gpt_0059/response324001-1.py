
from datetime import datetime

# Current time
now = datetime.now()

# Format the timestamp with rounded microseconds
formatted_time = now.strftime('%d-%m-%Y %H:%M:%S.') + f'{(now.microsecond // 10000):02d}'

print(formatted_time)
