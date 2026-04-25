
import datetime
from collections import defaultdict

# Given data
day_hour_pairs = {
    'Mon': [9, 23],
    'Thu': [12, 13, 14],
    'Tue': [11, 12, 14],
    'Wed': [11, 12, 13, 14],
    'Fri': [13],
    'Sat': [],
    'Sun': [],
}

start = datetime.datetime(2015, 7, 22, 17, 58, 54)
end = datetime.datetime(2015, 8, 30, 10, 22, 36)

def count_day_hour_pairs(start, end, pairs):
    # Adjust the start time to the beginning of the hour
    start = start.replace(minute=0, second=0, microsecond=0)
    # Adjust the end time to the end of the hour
    end = end.replace(minute=59, second=59, microsecond=999999)

    # Count occurrences
    count = defaultdict(int)

    current = start
    while current <= end:
        day_name = current.strftime('%a')  # Get the day of the week
        hour = current.hour

        if day_name in pairs and hour in pairs[day_name]:
            count[(day_name, hour)] += 1

        # Increment the hour
        current += datetime.timedelta(hours=1)

    return dict(count)

# Count for all day-hour pairs
result = count_day_hour_pairs(start, end, day_hour_pairs)
print("Count of day-hour pairs:", result)

# Specific case for Wednesdays at hour 14
def count_specific_day_hour(start, end, day_name, hour):
    count = 0
    current = start.replace(minute=0, second=0, microsecond=0)

    while current <= end:
        if current.strftime('%a') == day_name and current.hour == hour:
            count += 1
        current += datetime.timedelta(hours=1)

    return count

# Example for counting Wednesdays at hour 14
specific_count = count_specific_day_hour(start, end, 'Wed', 14)
print("Count of Wednesdays at hour 14:", specific_count)
