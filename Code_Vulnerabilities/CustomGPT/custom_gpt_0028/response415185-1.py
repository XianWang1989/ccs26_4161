
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

# Define the start and end datetime
start = datetime(2015, 7, 22, 17, 58, 54, 746784)
end = datetime(2015, 8, 30, 10, 22, 36, 363912)

# Function to count the occurrences of day-hour pairs
def count_day_hour_pairs(start, end, day_hour_pairs):
    # Prepare a default dictionary to count occurrences
    counts = defaultdict(int)

    # Current date for iteration
    current = start

    while current <= end:
        # Get the current day of the week
        day_name = current.strftime('%a')  # e.g., 'Mon', 'Tue', etc.

        # Check if the day is in our pairs
        if day_name in day_hour_pairs:
            for hour in day_hour_pairs[day_name]:
                # Count this hour if it falls within the start and end period
                if current.hour == hour:
                    counts[(day_name, hour)] += 1

        # Move to the next hour
        current += timedelta(hours=1)

    return counts

# Count occurrences and print
result = count_day_hour_pairs(start, end, day_hour_pairs)
for (day, hour), count in result.items():
    print(f"{count} occurrences of {day} at hour {hour}")
