
import datetime

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

def count_hours(start, end, day, hours):
    count = 0
    current = start

    # Create a mapping from weekday number to its name
    weekday_map = {0: 'Mon', 1: 'Tue', 2: 'Wed', 3: 'Thu', 4: 'Fri', 5: 'Sat', 6: 'Sun'}

    while current <= end:
        if current.strftime('%a') == day and current.hour in hours:
            count += 1
        # Move to the next hour
        current += datetime.timedelta(hours=1)

    return count

# Define your start and end datetime objects
start = datetime.datetime(2015, 7, 22, 17, 58, 54)
end = datetime.datetime(2015, 8, 30, 10, 22, 36)

# Count hours for multiple day-hour pairs
results = {}
for day, hours in day_hour_pairs.items():
    if hours:  # Only consider days with hours
        results[f'{day}'] = count_hours(start, end, day, hours)

print(results)
