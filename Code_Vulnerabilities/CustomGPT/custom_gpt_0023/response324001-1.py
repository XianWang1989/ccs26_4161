
from datetime import datetime

# Get the current timestamp
now = datetime.now()

# Format the timestamp with microseconds
formatted_timestamp = now.strftime('%d-%m-%Y %H:%M:%S.%f')

# Convert microseconds to tens of microseconds (round to 2 decimal places)
seconds, microseconds = formatted_timestamp.split('.')[:2]  # Split into main and microseconds
tens_of_microseconds = round(int(microseconds) / 1000, 2)  # Convert to tens of microseconds

# Combine the formatted string
final_timestamp = f"{seconds}.{int(tens_of_microseconds * 100):02}"

print(final_timestamp)  # Output: 03-07-2024 15:30:45.50 (example)
