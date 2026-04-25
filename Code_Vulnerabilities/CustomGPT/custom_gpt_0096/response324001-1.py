
import datetime

# Get current time with microseconds
current_time = datetime.datetime.now()

# Format the timestamp and round microseconds to 2 decimal places
formatted_time = current_time.strftime('%d-%m-%Y %H:%M:%S.') + f"{current_time.microsecond / 10000:02.0f}"

print(formatted_time)
