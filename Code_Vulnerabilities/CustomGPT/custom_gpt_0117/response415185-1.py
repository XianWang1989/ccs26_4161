
import datetime
from collections import defaultdict

# Define the day-of-week-hour pairs
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
    counts = defaultdict(int)

    current_datetime = start
    while current_datetime <= end:
        day_of_week = current_datetime.strftime('%a')  # Get abbreviated day name
        hour = current_datetime.hour

        if day_of_week in day_hour_pairs and hour in day_hour_pairs[day_of_week]:
            counts[(day_of_week, hour)] += 1

        # Move to the next hour
        current_datetime += datetime.timedelta(hours=1)

    return counts

# Get counts for each day-hour pair
result_counts = count_day_hour_pairs(start, end, day_hour_pairs)

# Print the counts
for (day, hour), count in result_counts.items():
    print(f"{day} {hour}: {count}")
