
from datetime import datetime, timedelta

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

# Define your start and end times
start = datetime(2015, 7, 22, 17, 58, 54, 746784)
end = datetime(2015, 8, 30, 10, 22, 36, 363912)

def count_day_hour_pairs(start, end, pairs):
    count = {day: 0 for day in pairs}

    # Iterate over each day from start to end
    current = start
    while current <= end:
        if current.strftime('%a') in pairs:
            current_hour = current.hour
            # Check if the current hour is in the corresponding day list
            if current_hour in pairs[current.strftime('%a')]:
                count[current.strftime('%a')] += 1
        current += timedelta(hours=1)

    return count

# Get the count for each day-hour pair
result = count_day_hour_pairs(start, end, day_hour_pairs)
print(result)

# For the simpler case of counting Wednesdays at 14
def count_specific_day_hour(start, end, day, hour):
    count = 0
    current = start
    while current <= end:
        if current.strftime('%a') == day and current.hour == hour:
            count += 1
        current += timedelta(hours=1)
    return count

# Count number of Wednesdays at 14:00
wednesday_count = count_specific_day_hour(start, end, 'Wed', 14)
print(f'Count of Wednesdays at 14:00: {wednesday_count}')
