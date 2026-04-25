
from datetime import datetime

# Current timestamp
now = datetime.now()

# Format the timestamp to include microseconds
formatted_timestamp = now.strftime('%d-%m-%Y %H:%M:%S.%f')

# Convert microseconds to two decimal places (tenths of a millisecond)
# Split before the microseconds part and get only the first 2 digits of the microseconds
formatted_timestamp = formatted_timestamp[:-3] + formatted_timestamp[-3:-1]

# Print the result
print(formatted_timestamp)
