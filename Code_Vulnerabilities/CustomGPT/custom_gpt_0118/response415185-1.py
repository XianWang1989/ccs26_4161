
import datetime
from collections import defaultdict

# Define the day-of-week-hour pairs
day_hour_pairs = {
    'Mon': [9, 23],
    'Tue': [11, 12, 14],
    'Wed': [11, 12, 13, 14],
    'Thu': [12, 13, 14],
    'Fri': [13],
    'Sat': [],
    'Sun': [],
}

def count_day_hour_pairs(start, end, day_hour_pairs):
    current = start
    counts = defaultdict(int)

    while current <= end:
        day_name = current.strftime('%a')  # Get abbreviated weekday name

        if day_name in day_hour_pairs:
            for hour in day_hour_pairs[day_name]:
                if current.hour == hour:
                    counts[(day_name, hour)] += 1

        # Move to the next hour
        current += datetime.timedelta(hours=1)

    return counts

# Define the start and end times
start_time = datetime.datetime(2015, 7, 22, 17, 58, 54, 746784)
end_time = datetime.datetime(2015, 8, 30, 10, 22, 36, 363912)

# Count the occurrences
result = count_day_hour_pairs(start_time, end_time, day_hour_pairs)

# Print the results
for (day, hour), count in result.items():
    print(f"{day} {hour}: {count} occurrences")
