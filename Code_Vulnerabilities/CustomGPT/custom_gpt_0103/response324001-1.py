
from datetime import datetime

# Current timestamp
now = datetime.now()

# Format with 2 decimal places for microseconds
formatted_time = now.strftime('%d-%m-%Y %H:%M:%S.') + f'{now.microsecond // 10000:02d}'

print(formatted_time)
