
from datetime import datetime, timedelta

# Example timestamp
timestamp = datetime.now()

# Get the microseconds and convert to tens of microseconds
tens_of_microseconds = (timestamp.microsecond // 10000) * 10

# Create a formatted string with rounded tens of microseconds
formatted_time = timestamp.strftime('%d-%m-%Y %H:%M:%S.') + f'{tens_of_microseconds:02d}'

print(formatted_time)
