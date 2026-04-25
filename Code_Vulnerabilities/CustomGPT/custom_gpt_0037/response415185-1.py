
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

def count_day_hour_pairs(start, end, pairs):
    # Initialize a dictionary to count occurrences
    counts = defaultdict(int)

    # Loop through each day of the week
    delta = datetime.timedelta(days=1)
    current_time = start

    while current_time <= end:
        day = current_time.strftime('%a')  # Get the current day of the week
        hour = current_time.hour            # Get the current hour

        # Check if the current day and hour are in the given pairs
        if day in pairs and hour in pairs[day]:
            counts[(day, hour)] += 1

        # Move to the next hour
        current_time += datetime.timedelta(hours=1)

    return counts

# Example datetime objects
start = datetime.datetime(2015, 7, 22, 17, 58, 54)
end = datetime.datetime(2015, 8, 30, 10, 22, 36)

# Count occurrences
result = count_day_hour_pairs(start, end, day_hour_pairs)

# Display results
for key, count in result.items():
    print(f"{key}: {count}")
