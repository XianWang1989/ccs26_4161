
import datetime

# Define the day-hour pairs
day_hour_pairs = {
    'Mon': [9, 23],
    'Thu': [12, 13, 14],
    'Tue': [11, 12, 14],
    'Wed': [11, 12, 13, 14],
    'Fri': [13],
    'Sat': [],
    'Sun': []
}

def count_day_hour_pairs(start, end, pairs):
    # Initialize a dictionary to hold counts
    counts = {day: 0 for day in pairs.keys()}

    # Iterate over the date range
    current = start
    while current <= end:
        day_name = current.strftime('%a')  # Get the day name (e.g., 'Mon', 'Tue')
        hour = current.hour  # Get the current hour

        # Check if the current day and hour are in the specified pairs
        if day_name in pairs and hour in pairs[day_name]:
            counts[day_name] += 1

        # Move to the next hour
        current += datetime.timedelta(hours=1)

    return counts

# Given start and end datetimes
start = datetime.datetime(2015, 7, 22, 17, 58, 54)
end = datetime.datetime(2015, 8, 30, 10, 22, 36)

# Count the day-hour pairs
result = count_day_hour_pairs(start, end, day_hour_pairs)

print(result)
