
import datetime

# Define the day-hour pairs
day_hour_pairs = {
    'Mon': [9, 23],
    'Thu': [12, 13, 14],
    'Tue': [11, 12, 14],
    'Wed': [11, 12, 13, 14],
    'Fri': [13],
    'Sat': [],
    'Sun': [],
}

# Define the start and end datetime
start = datetime.datetime(2015, 7, 22, 17, 58, 54, 746784)
end = datetime.datetime(2015, 8, 30, 10, 22, 36, 363912)

# Initialize the counter
hour_count = {day: 0 for day in day_hour_pairs.keys()}

# Iterate through each day in the date range
current_date = start
while current_date <= end:
    day_name = current_date.strftime('%a')  # Get day of the week as 'Mon', 'Tue', etc.
    if day_name in day_hour_pairs:
        for hour in day_hour_pairs[day_name]:
            # Create a datetime object for that hour
            hour_datetime = current_date.replace(hour=hour, minute=0, second=0, microsecond=0)
            # Check if the hour falls within the range
            if start <= hour_datetime <= end:
                hour_count[day_name] += 1

    # Move to the next day
    current_date += datetime.timedelta(days=1)

# Print results
print(hour_count)
