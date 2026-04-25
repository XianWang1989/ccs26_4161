
import datetime
from collections import defaultdict

# Sample day-of-week-hour pairs
day_hour_pairs = {
    'Mon': [9, 23],
    'Tue': [11, 12, 14],
    'Wed': [11, 12, 13, 14],
    'Thu': [12, 13, 14],
    'Fri': [13],
    'Sat': [],
    'Sun': [],
}

def count_hours(start, end, day_hour_dict):
    # Create a defaultdict to hold counts
    counts = defaultdict(int)

    # Traverse through the date range
    current = start
    while current <= end:
        day_name = current.strftime('%a')  # Get day of the week
        if day_name in day_hour_dict:
            for hour in day_hour_dict[day_name]:
                if current.hour == hour:
                    counts[(day_name, hour)] += 1
        current += datetime.timedelta(hours=1)  # Increment by one hour

    return counts

# Example usage
start = datetime.datetime(2015, 7, 22, 17, 58, 54)
end = datetime.datetime(2015, 8, 30, 10, 22, 36)

result_counts = count_hours(start, end, day_hour_pairs)

# Print results
for key, count in result_counts.items():
    print(f"{key}: {count}")
