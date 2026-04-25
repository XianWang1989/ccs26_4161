
from datetime import datetime

# Current timestamp
now = datetime.now()

# Get microseconds, divide by 10,000 to convert to tens of microseconds and round
tens_of_microsecs = round(now.microsecond / 10000, 2)

# Format the timestamp with rounded microseconds
formatted_time = now.strftime(f'%d-%m-%Y %H:%M:%S.{int(tens_of_microsecs):02}')

print(formatted_time)
