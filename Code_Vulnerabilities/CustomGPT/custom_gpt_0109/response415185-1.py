
from datetime import datetime, timedelta
import collections

# Define the day/hour pairs
day_hour_pairs = {
    'Mon': [9, 23],
    'Tue': [11, 12, 14],
    'Wed': [11, 12, 13, 14],
    'Thu': [12, 13, 14],
    'Fri': [13],
    'Sat': [],
    'Sun': []
}

# Define the start and end datetime
start = datetime(2015, 7, 22, 17, 58, 54, 746784)
end = datetime(2015, 8, 30, 10, 22, 36, 363912)

def count_occurrences(start, end, day_hour_pairs):
    # Create a dictionary to hold the counts
    counts = collections.defaultdict(int)

    # Iterate over each day-hour pair
    current = start
    while current <= end:
        weekday = current.strftime("%a")  # Get the day of the week
        hour = current.hour                # Get the current hour

        # Check if the current day and hour are in the pairs
        if weekday in day_hour_pairs and hour in day_hour_pairs[weekday]:
            counts[(weekday, hour)] += 1

        # Move to the next hour
        current += timedelta(hours=1)

    return counts

# Count the occurrences for the specified day-hour pairs
occurrences = count_occurrences(start, end, day_hour_pairs)

# Print the results
for (day, hour), count in occurrences.items():
    print(f"{day} at {hour}:00 --> {count} occurrences")
