
import datetime
from collections import defaultdict

# Define the day-of-week-hour pairs
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
start = datetime.datetime(2015, 7, 22, 17, 58, 54, 746784)
end = datetime.datetime(2015, 8, 30, 10, 22, 36, 363912)

# Function to count occurrences of day-hour pairs
def count_day_hour_pairs(start, end, pairs):
    counts = defaultdict(int)
    current = start

    # Move to next hour within the range
    while current <= end:
        day_name = current.strftime('%a')  # Get day name (Mon, Tue, etc.)
        if day_name in pairs:
            if current.hour in pairs[day_name]:
                counts[(day_name, current.hour)] += 1
        current += datetime.timedelta(hours=1)

    return counts

# Count the occurrences
result = count_day_hour_pairs(start, end, day_hour_pairs)

# Output result
print("Counts for each day-hour pair:")
for (day, hour), count in result.items():
    print(f"{day} {hour}: {count}")

# Specific case for "Wednesdays at 14"
specific_day = 'Wed'
specific_hour = 14
specific_count = result.get((specific_day, specific_hour), 0)
print(f"\nNumber of {specific_day} at {specific_hour}:00 between the dates: {specific_count}")
