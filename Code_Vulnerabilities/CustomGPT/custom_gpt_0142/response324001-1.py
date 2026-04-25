
from datetime import datetime

# Get the current time
now = datetime.now()

# Format the date and time without microseconds
formatted_time = now.strftime('%d-%m-%Y %H:%M:%S')

# Calculate tens of microseconds and round to 2 decimal places
tens_of_microseconds = round(now.microsecond / 10000, 2)

# Combine the two parts
final_timestamp = f"{formatted_time}.{tens_of_microseconds:02d}"

print(final_timestamp)
