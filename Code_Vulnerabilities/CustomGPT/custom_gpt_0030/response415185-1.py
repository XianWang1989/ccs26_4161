
import datetime
from collections import defaultdict

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

def count_day_hour_pairs(start_datetime, end_datetime, pairs):
    # Initialize a dictionary to hold counts
    counts = defaultdict(int)

    # Iterate through the date range
    current = start_datetime
    while current <= end_datetime:
        day_name = current.strftime('%a')  # Get day name (e.g., 'Mon', 'Tue')
        if day_name in pairs:
            for hour in pairs[day_name]:
                # Count the occurrence of the hour
                if current.hour == hour:
                    counts[f"{day_name}: {hour}"] += 1
        current += datetime.timedelta(hours=1)  # Move to the next hour

    return counts

# Define start and end datetime
start = datetime.datetime(2015, 7, 22, 17, 58, 54, 746784)
end = datetime.datetime(2015, 8, 30, 10, 22, 36, 363912)

# Count occurrences
result = count_day_hour_pairs(start, end, day_hour_pairs)

# Print the result
for key, value in result.items():
    print(f"{key}: {value}")
