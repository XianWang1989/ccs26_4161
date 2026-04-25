
from datetime import datetime, timedelta
import collections

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

# Define the start and end datetimes
start = datetime(2015, 7, 22, 17, 58, 54, 746784)
end = datetime(2015, 8, 30, 10, 22, 36, 363912)

def count_day_hour_pairs(day_hour_pairs, start, end):
    count = collections.defaultdict(int)

    current = start
    one_hour = timedelta(hours=1)

    # Iterate through the range of dates
    while current <= end:
        day_name = current.strftime('%a')
        hour = current.hour

        # Check if the current hour falls into the specified pairs
        if hour in day_hour_pairs.get(day_name, []):
            count[(day_name, hour)] += 1

        current += one_hour

    return count

result = count_day_hour_pairs(day_hour_pairs, start, end)

# Display the result
for k, v in result.items():
    print(f"{k}: {v}")
