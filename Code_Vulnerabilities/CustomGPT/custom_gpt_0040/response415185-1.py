
from datetime import datetime, timedelta
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

def count_day_hour_pairs(start, end, day_hour_pairs):
    # Dictionary to store counts
    counts = defaultdict(int)

    current = start
    while current <= end:
        day_name = current.strftime('%a')  # Get the day name (Mon, Tue, ...)
        hour = current.hour

        if day_name in day_hour_pairs and hour in day_hour_pairs[day_name]:
            counts[(day_name, hour)] += 1

        current += timedelta(hours=1)  # Move to the next hour

    return counts

# Example datetime objects
start = datetime(2015, 7, 22, 17, 58, 54)
end = datetime(2015, 8, 30, 10, 22, 36)

# Count day-hour pairs
result = count_day_hour_pairs(start, end, day_hour_pairs)

# Print the result
for (day, hour), count in result.items():
    print(f"{count} occurrences of {day}: {hour}")
