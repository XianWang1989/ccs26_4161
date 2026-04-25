
import datetime
from collections import defaultdict

def count_day_hour_pairs(start, end, day_hour_map):
    day_hour_count = defaultdict(int)

    current = start
    while current <= end:
        if current.strftime('%a') in day_hour_map:
            if current.hour in day_hour_map[current.strftime('%a')]:
                day_hour_count[(current.strftime('%a'), current.hour)] += 1
        current += datetime.timedelta(hours=1)

    return dict(day_hour_count)

# Define the day-hour pairs
day_hour_map = {
    'Mon': [9, 23],
    'Thu': [12, 13, 14],
    'Tue': [11, 12, 14],
    'Wed': [11, 12, 13, 14],
    'Fri': [13],
    'Sat': [],
    'Sun': [],
}

# Define the start and end datetime
start = datetime.datetime(2015, 7, 22, 17, 58, 54)
end = datetime.datetime(2015, 8, 30, 10, 22, 36)

# Count the occurrences
result = count_day_hour_pairs(start, end, day_hour_map)

# Output the result
for (day, hour), count in result.items():
    print(f"{day} at {hour}: {count}")
