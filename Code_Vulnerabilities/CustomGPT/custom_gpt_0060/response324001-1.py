
from datetime import datetime

# Get the current datetime
now = datetime.now()

# Format the timestamp to include microseconds
formatted_timestamp = now.strftime('%d-%m-%Y %H:%M:%S.%f')

# Round the microseconds to 2 decimal places and convert to tens of microseconds
# Divide by 10 to convert to tens of microseconds and round to 2 decimal places
tens_of_microseconds = round(int(now.microsecond) / 10, 2)

# Combine the formatted timestamp with the rounded microseconds
# Extract the first 20 characters to include date and time
# Append the rounded microseconds formatted to 2 decimal places
final_timestamp = f"{formatted_timestamp[:-6]}{tens_of_microseconds:.2f}"

print(final_timestamp)
