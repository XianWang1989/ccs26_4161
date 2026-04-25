
from datetime import datetime, timedelta

# Define your datetime range
start = datetime(2015, 7, 22, 17, 58, 54)
end = datetime(2015, 8, 30, 10, 22, 36)

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

def count_day_hour_pairs(start, end, day_hour_pairs):
    count = {}
    current = start

    while current <= end:
        day_name = current.strftime('%a')
        if day_name in day_hour_pairs:
            for hour in day_hour_pairs[day_name]:
                if current.hour == hour:
                    count[(day_name, hour)] = count.get((day_name, hour), 0) + 1

        # Move to the next hour
        current += timedelta(hours=1)

    return count

# Count occurrences for each day-hour pair
result = count_day_hour_pairs(start, end, day_hour_pairs)

# Display the results
for k, v in result.items():
    print(f'{k}: {v}')
