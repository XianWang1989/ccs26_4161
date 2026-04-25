
from datetime import datetime

# Get the current timestamp
now = datetime.now()

# Format the timestamp
formatted_time = now.strftime('%d-%m-%Y %H:%M:%S.')

# Get the microseconds and convert to tens of microseconds
tens_of_microseconds = now.microsecond // 10000  # Floor division to convert

# Format and round to 2 decimal places (for display)
formatted_time += f"{tens_of_microseconds:02d}"

print(formatted_time)
