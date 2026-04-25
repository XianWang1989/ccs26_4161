
from datetime import datetime

# Current timestamp
now = datetime.now()

# Format the timestamp
formatted_timestamp = now.strftime('%d-%m-%Y %H:%M:%S.')

# Get microseconds, divide by 10, and round to 2 decimal places
tens_of_microseconds = round(now.microsecond / 10 ** 4, 2)

# Combine formatted parts and the rounded microseconds
result = f"{formatted_timestamp}{tens_of_microseconds:02d}"

print(result)
