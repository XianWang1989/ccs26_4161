
from datetime import datetime

# Current timestamp
now = datetime.now()

# Convert microseconds to tens of microseconds and round
tens_of_microseconds = round(now.microsecond / 10000)

# Construct the formatted timestamp
formatted_timestamp = now.strftime('%d-%m-%Y %H:%M:%S.') + f'{tens_of_microseconds:02}'

print(formatted_timestamp)
