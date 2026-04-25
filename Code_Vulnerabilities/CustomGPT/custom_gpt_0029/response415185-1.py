
from datetime import datetime, timedelta
from collections import defaultdict

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
start = datetime(2015, 7, 22, 17, 58, 54, 746784)
end = datetime(2015, 8, 30, 10, 22, 36, 363912)

# Function to count day-hour occurrences
def count_day_hour_pairs(start, end, day_hour_pairs):
    current = start
    counts = defaultdict(int)

    while current <= end:
        # Get the day of the week and the hour
        day_name = current.strftime('%a')  # 'Mon', 'Tue', etc.
        hour = current.hour

        # Increment the count if the day-hour pair exists
        if day_name in day_hour_pairs and hour in day_hour_pairs[day_name]:
            counts[(day_name, hour)] += 1

        # Move to the next hour
        current += timedelta(hours=1)

    return counts

# Count occurrences
results = count_day_hour_pairs(start, end, day_hour_pairs)

# Print the results
for (day, hour), count in results.items():
    print(f"{day}: {hour} -> {count} occurrences")
