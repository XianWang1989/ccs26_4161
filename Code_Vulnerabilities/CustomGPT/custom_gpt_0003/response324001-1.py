
from datetime import datetime

# Get the current time
now = datetime.now()

# Format the timestamp without microseconds
timestamp = now.strftime('%d-%m-%Y %H:%M:%S')

# Extract microseconds and round to two decimal places
# Divide microseconds by 10000 to convert to tens of microseconds
rounded_microseconds = round(now.microsecond / 10000, 2)

# Format the final output
final_timestamp = f"{timestamp}.{int(rounded_microseconds):02}"
print(final_timestamp)
