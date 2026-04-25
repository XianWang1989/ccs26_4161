
import datetime

# Define the day-hour pairs
day_hour_pairs = {
    'Mon': [9, 23],
    'Tue': [11, 12, 14],
    'Wed': [11, 12, 13, 14],
    'Thu': [12, 13, 14],
    'Fri': [13],
    'Sat': [],
    'Sun': [],
}

# Define the start and end datetimes
start = datetime.datetime(2015, 7, 22, 17, 58, 54)
end = datetime.datetime(2015, 8, 30, 10, 22, 36)

def count_day_hour_pairs(start, end, day_hour_pairs):
    # Initialize counts
    counts = {key: 0 for key in day_hour_pairs}

    # Create a current date variable starting from the start date
    current = start

    # Iterate through the days between start and end
    while current <= end:
        # Get current day of the week and hour
        day_name = current.strftime('%a')  # Short weekday name (e.g., 'Wed')
        hour = current.hour

        # Check if the current hour is in the defined pairs for this day
        if day_name in day_hour_pairs and hour in day_hour_pairs[day_name]:
            counts[day_name] += 1

        # Move to the next hour
        current += datetime.timedelta(hours=1)

    return counts

# Get the counts for the specified time range
result = count_day_hour_pairs(start, end, day_hour_pairs)
print(result)
