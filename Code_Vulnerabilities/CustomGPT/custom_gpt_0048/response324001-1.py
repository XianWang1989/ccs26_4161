
from datetime import datetime

# Get the current time
now = datetime.now()

# Round microseconds to tens of microseconds (i.e., 2 decimal places)
microseconds = round(now.microsecond / 10000)  # Convert to tens of microseconds
formatted_time = now.strftime(f'%d-%m-%Y %H:%M:%S.{microseconds:02}0')

print(formatted_time)
