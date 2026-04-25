
from datetime import datetime

# Get the current time
now = datetime.now()

# Format the time string
formatted_time = now.strftime('%d-%m-%Y %H:%M:%S')

# Calculate microseconds in tens
tens_of_microseconds = round(now.microsecond / 10000, 2)

# Combine the formatted time with the rounded tens of microseconds
result = f"{formatted_time}.{int(tens_of_microseconds):02}"

print(result)
