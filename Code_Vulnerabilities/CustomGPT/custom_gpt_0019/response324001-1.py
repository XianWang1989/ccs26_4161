
from datetime import datetime

# Current timestamp
now = datetime.now()

# Format timestamp with microseconds rounded to two decimal places (in tens of microseconds)
timestamp = now.strftime('%d-%m-%Y %H:%M:%S.')
microseconds_tens = f"{now.microsecond // 10000:02d}"  # Convert to tens of microseconds
formatted_timestamp = f"{timestamp}{microseconds_tens}"

print(formatted_timestamp)
