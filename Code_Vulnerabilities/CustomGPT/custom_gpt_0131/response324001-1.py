
from datetime import datetime

# Get the current timestamp
now = datetime.now()

# Extract the microseconds and convert to tens of microseconds
tens_of_microseconds = round(now.microsecond / 10000, 2)  # convert to tens of microseconds

# Format the timestamp string manually
formatted_timestamp = now.strftime('%d-%m-%Y %H:%M:%S') + f'.{int(tens_of_microseconds):02d}'

print(formatted_timestamp)
