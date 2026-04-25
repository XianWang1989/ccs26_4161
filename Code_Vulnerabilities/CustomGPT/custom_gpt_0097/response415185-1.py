
from datetime import datetime, timedelta

def count_day_hour_pairs(start, end, day_hour_pairs):
    result = {}
    days_of_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    # Create a mapping of day names to weekdays
    day_mapping = {day: i for i, day in enumerate(days_of_week)}

    # Initialize result dictionary
    for day, hours in day_hour_pairs.items():
        result[day] = {hour: 0 for hour in hours}

    # Iterate through each day in the range
    current = start
    while current <= end:
        if current.strftime('%a') in day_hour_pairs:
            for hour in day_hour_pairs[current.strftime('%a')]:
                if current.hour == hour:
                    result[current.strftime('%a')][hour] += 1
        current += timedelta(hours=1)

    return result

# Example usage
start = datetime(2015, 7, 22, 17, 58)
end = datetime(2015, 8, 30, 10, 22)

day_hour_pairs = {
    'Mon': [9, 23],
    'Thu': [12, 13, 14],
    'Tue': [11, 12, 14],
    'Wed': [11, 12, 13, 14],
    'Fri': [13],
    'Sat': [],
    'Sun': [],
}

result = count_day_hour_pairs(start, end, day_hour_pairs)
print(result)
