
from datetime import datetime

# Get current timestamp
now = datetime.now()

# Format the timestamp
formatted_timestamp = now.strftime('%d-%m-%Y %H:%M:%S')

# Calculate microseconds and round to 2 decimal places
rounded_microseconds = round(now.microsecond / 10000)  # Convert to tens of microseconds
formatted_timestamp += f".{rounded_microseconds:02d}"  # Format to two decimal places

print(formatted_timestamp)
