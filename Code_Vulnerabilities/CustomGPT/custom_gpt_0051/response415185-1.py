
import datetime
from collections import Counter

def count_day_hour(start, end, day_hour_pairs):
    current = start
    counts = Counter()

    while current <= end:
        # Get the day of the week and hour
        day_name = current.strftime('%a')  # Mon, Tue, etc.
        hour = current.hour

        # Check if this day and hour are in the pairs
        if day_name in day_hour_pairs and hour in day_hour_pairs[day_name]:
            counts[(day_name, hour)] += 1

        # Move to the next hour
        current += datetime.timedelta(hours=1)

    return counts

# Define your day-hour dictionary
day_hour_pairs = {
    'Mon': [9, 23],
    'Thu': [12, 13, 14],
    'Tue': [11, 12, 14],
    'Wed': [11, 12, 13, 14],
    'Fri': [13],
    'Sat': [],
    'Sun': [],
}

# Define your start and end datetime
start_datetime = datetime.datetime(2015, 7, 22, 17, 58, 54)
end_datetime = datetime.datetime(2015, 8, 30, 10, 22, 36)

# Count occurrences
counts = count_day_hour(start_datetime, end_datetime, day_hour_pairs)

# Print results
for key, value in counts.items():
    print(f"{key}: {value}")
