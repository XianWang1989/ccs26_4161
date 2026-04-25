
import datetime
from collections import defaultdict

# Define your day-hour pairs
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

# Function to count occurrences of a specific day-hour pair
def count_specific_day_hour(start, end, day, hour):
    count = 0
    current = start

    # Move to the next hour date-time if start is not at the hour
    if start.hour > hour:
        current = (start + datetime.timedelta(days=1)).replace(hour=hour, minute=0, second=0, microsecond=0)
    elif start.hour < hour:
        current = start.replace(hour=hour, minute=0, second=0, microsecond=0)

    # Loop through days until we reach the end
    while current <= end:
        if current.strftime('%a') == day and current.hour == hour:
            count += 1
        current += datetime.timedelta(hours=1)

    return count

# Example for counting Wednesdays at 14:00
wednesday_count = count_specific_day_hour(start, end, 'Wed', 14)
print("Wednesdays at 14:00:", wednesday_count)

# To count for all day-hour pairs
def count_all_day_hour_pairs(start, end, day_hour_pairs):
    total_counts = defaultdict(int)

    for day, hours in day_hour_pairs.items():
        for hour in hours:
            count = count_specific_day_hour(start, end, day, hour)
            total_counts[f"{day} at {hour}"] = count

    return total_counts

# Count for all pairs
all_counts = count_all_day_hour_pairs(start, end, day_hour_pairs)
for k, v in all_counts.items():
    print(f"{k}: {v}")
