
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

# Define the start and end datetime
start = datetime.datetime(2015, 7, 22, 17, 58, 54, 746784)
end = datetime.datetime(2015, 8, 30, 10, 22, 36, 363912)

def count_day_hour_pairs(start, end, day_hour_pairs):
    count = defaultdict(int)  # Dictionary to hold counts for each day-hour pair
    current = start

    # Loop through the range by hour
    while current <= end:
        day_name = current.strftime('%a')  # Get the day name (Mon, Tue, ...)
        hour = current.hour  # Get the hour

        # Check if this day and hour are in the pairs
        if hour in day_hour_pairs.get(day_name, []):
            count[(day_name, hour)] += 1

        # Move to the next hour
        current += datetime.timedelta(hours=1)

    return count

# Count occurrences of each day-hour pair
result = count_day_hour_pairs(start, end, day_hour_pairs)

# Print results
for (day, hour), total in result.items():
    print(f"{total} occurrences of {day}: {hour}")
