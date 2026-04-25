
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

# Define the start and end datetime
start = datetime.datetime(2015, 7, 22, 17, 58, 54, 746784)
end = datetime.datetime(2015, 8, 30, 10, 22, 36, 363912)

# Count occurrences
def count_day_hour_pairs(start, end, pairs):
    current = start
    counts = defaultdict(int)

    while current <= end:
        day_name = current.strftime('%a')  # Get day name (Mon, Tue, etc.)
        if day_name in pairs:
            # Check if current hour matches
            if current.hour in pairs[day_name]:
                counts[(day_name, current.hour)] += 1
        current += datetime.timedelta(hours=1)

    return counts

# Get the counts
result = count_day_hour_pairs(start, end, day_hour_pairs)
print(result)
