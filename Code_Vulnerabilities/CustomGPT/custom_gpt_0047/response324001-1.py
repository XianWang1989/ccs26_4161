
from datetime import datetime

# Get the current timestamp
now = datetime.now()

# Format the timestamp with rounded microseconds to 2 decimal places
formatted_timestamp = now.strftime('%d-%m-%Y %H:%M:%S.') + f'{int(now.microsecond / 10000):02}'

# Print the formatted timestamp
print(formatted_timestamp)
