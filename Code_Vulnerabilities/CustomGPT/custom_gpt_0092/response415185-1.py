
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
    counts = defaultdict(int)

    # Iterate through the date range
    current = start
    while current <= end:
        day_name = current.strftime('%a')  # Get the day of the week as a short name
        hour = current.hour

        # If the current day has specified hours
        if day_name in pairs and hour in pairs[day_name]:
            counts[(day_name, hour)] += 1

        # Move to the next hour
        current += datetime.timedelta(hours=1)

    return counts

# Define start and end datetime
start = datetime.datetime(2015, 7, 22, 17, 58, 54, 746784)
end = datetime.datetime(2015, 8, 30, 10, 22, 36, 363912)

# Count occurrences
counts = count_day_hour_pairs(start, end, day_hour_pairs)

# Display results
for (day, hour), count in counts.items():
    print(f"{day} at {hour}:00 - {count} occurrences")

# Example for counting specific 'Wednesday: 14'
def count_specific_day_hour(start, end, day, hour):
    count = 0
    current = start

    while current <= end:
        if current.strftime('%a') == day and current.hour == hour:
            count += 1
        current += datetime.timedelta(hours=1)

    return count

# Count occurrences for 'Wednesday: 14'
specific_count = count_specific_day_hour(start, end, 'Wed', 14)
print(f"Wednesdays at 14:00 - {specific_count} occurrences")
