
import datetime
from collections import defaultdict

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

def count_day_hour_pairs(start, end, pairs):
    # Initialize the counts
    hour_counts = defaultdict(int)
    # Create a set of day names for easy lookup
    days = list(pairs.keys())

    # Iterate through each day in the range
    current = start
    while current <= end:
        if current.strftime('%a') in days:
            day_name = current.strftime('%a')
            if current.hour in pairs[day_name]:
                hour_counts[(day_name, current.hour)] += 1
        current += datetime.timedelta(hours=1)

    return hour_counts

# Sample start and end datetime objects
start = datetime.datetime(2015, 7, 22, 17, 58, 54)
end = datetime.datetime(2015, 8, 30, 10, 22, 36)

# Count the hours
result = count_day_hour_pairs(start, end, day_hour_pairs)
print(dict(result))
