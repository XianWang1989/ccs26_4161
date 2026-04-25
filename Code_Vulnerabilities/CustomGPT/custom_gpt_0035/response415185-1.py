
import datetime
from collections import defaultdict

# Function to count occurrences for a single day-hour pair
def count_specific_day_hour(start, end, day, hour):
    count = 0
    current = start

    while current <= end:
        if current.strftime('%a') == day and current.hour == hour:
            count += 1
        current += datetime.timedelta(hours=1)

    return count

# Function to count occurrences for a dictionary of day-hour pairs
def count_day_hour_pairs(start, end, day_hour_dict):
    results = defaultdict(int)

    current = start
    while current <= end:
        day_name = current.strftime('%a')
        if day_name in day_hour_dict:
            for hour in day_hour_dict[day_name]:
                if current.hour == hour:
                    results[(day_name, hour)] += 1
        current += datetime.timedelta(hours=1)

    return results

# Example datetime objects
start = datetime.datetime(2015, 7, 22, 17, 58, 54)
end = datetime.datetime(2015, 8, 30, 10, 22, 36)

# Day-hour pairs definition
day_hour_pairs = {
    'Mon': [9, 23],
    'Thu': [12, 13, 14],
    'Tue': [11, 12, 14],
    'Wed': [11, 12, 13, 14],
    'Fri': [13],
    'Sat': [],
    'Sun': [],
}

# Count occurrences for a single pair (e.g., Wednesdays at 14)
wednesday_14_count = count_specific_day_hour(start, end, 'Wed', 14)
print(f'Wednesdays at 14: {wednesday_14_count}')

# Count occurrences for all day-hour pairs
all_counts = count_day_hour_pairs(start, end, day_hour_pairs)
print('Occurrences for all day-hour pairs:')
for (day, hour), count in all_counts.items():
    print(f'{day} at {hour}: {count}')
