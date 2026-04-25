
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

def count_hours(start, end, day_hour_dict):
    # Create a defaultdict to hold counts
    hour_counts = defaultdict(int)

    # Adjust start to next hour if not on the hour
    if start.minute != 0 or start.second != 0:
        start += datetime.timedelta(hours=1)
        start = start.replace(minute=0, second=0, microsecond=0)

    # Looping through each hour in the range
    current_time = start
    while current_time <= end:
        if current_time.weekday() in range(len(day_hour_dict)):  # 0=Mon, 1=Tue, ...
            day_name = list(day_hour_dict.keys())[current_time.weekday()]
            current_hour = current_time.hour
            # Only count if the current hour is in the defined hours for that day
            if current_hour in day_hour_dict[day_name]:
                hour_counts[day_name] += 1
        current_time += datetime.timedelta(hours=1)

    return hour_counts

# Example usage
start_time = datetime.datetime(2015, 7, 22, 17, 58, 54)
end_time = datetime.datetime(2015, 8, 30, 10, 22, 36)

result = count_hours(start_time, end_time, day_hour_pairs)
print(result)
