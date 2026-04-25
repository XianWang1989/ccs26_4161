
from datetime import datetime

# Get the current timestamp
now = datetime.now()

# Format to include microseconds then round them to 2 decimal places
formatted_time = now.strftime('%d-%m-%Y %H:%M:%S.') + f'{now.microsecond / 10000:.0f}'

print(formatted_time)
