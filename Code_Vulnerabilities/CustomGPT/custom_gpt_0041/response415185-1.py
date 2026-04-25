
import datetime
from collections import defaultdict

# Define your day-hour pairs
day_hour_pairs = {
    'Mon': [9, 23],
    'Tue': [11, 12, 14],
    'Wed': [11, 12, 13, 14],
    'Thu': [12, 13, 14],
    'Fri': [13],
    'Sat': [],
    'Sun': [],
}

# Function to count hours for a specific day-hour pair
def count_hours(day, hour, start, end):
    count = 0
    current = start

    while current <= end:
        if current.strftime('%a') == day and current.hour == hour:
            count += 1
        current += datetime.timedelta(hours=1)

    return count

# Function to count hours for all day-hour pairs
def count_day_hour_pairs(start, end, pairs):
    total_hours = defaultdict(int)

    for day, hours in pairs.items():
        for hour in hours:
            total_hours[(day, hour)] = count_hours(day, hour, start, end)

    return total_hours

# Example datetime points
start = datetime.datetime(2015, 7, 22, 17, 58, 54)
end = datetime.datetime(2015, 8, 30, 10, 22, 36)

# Count hours for all day-hour pairs
result = count_day_hour_pairs(start, end, day_hour_pairs)

# Print the results
for (day, hour), count in result.items():
    print(f"{day} at {hour}:00 -> {count} occurrences")
