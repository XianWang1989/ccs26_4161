
import datetime
from collections import defaultdict

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

def count_day_hour_pairs(start, end, pairs):
    count = defaultdict(int)

    # Iterate through each day from start to end
    current = start
    while current <= end:
        if current.strftime('%a') in pairs:
            hour = current.hour
            if hour in pairs[current.strftime('%a')]:
                count[current.strftime('%a'), hour] += 1
        current += datetime.timedelta(hours=1)

    return count

# Example usage
start = datetime.datetime(2015, 7, 22, 17, 58, 54)
end = datetime.datetime(2015, 8, 30, 10, 22, 36)

result = count_day_hour_pairs(start, end, day_hour_pairs)

# Print results for specific pairs
specific_day_hour = ('Wed', 14)
print(f"Count of {specific_day_hour}: {result.get(specific_day_hour, 0)}")
