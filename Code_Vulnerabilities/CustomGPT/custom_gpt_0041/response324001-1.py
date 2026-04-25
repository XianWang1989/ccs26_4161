
from datetime import datetime

# Current timestamp
now = datetime.now()

# Format the timestamp
formatted_time = now.strftime('%d-%m-%Y %H:%M:%S.')

# Get microseconds, convert to tens of microseconds and format
tens_of_microseconds = round(now.microsecond / 10000)  # 10000 microseconds = 10 milliseconds
formatted_time += f'{tens_of_microseconds:02d}'

print(formatted_time)
