
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

# Define the start and end datetime
start = datetime.datetime(2015, 7, 22, 17, 58, 54)
end = datetime.datetime(2015, 8, 30, 10, 22, 36)

# Function to count occurrences for day-hour pairs
def count_day_hour_occurrences(start, end, day_hour_pairs):
    count = defaultdict(int)
    current = start

    while current <= end:
        day_name = current.strftime('%a')  # Get the day of the week
        if day_name in day_hour_pairs:
            for hour in day_hour_pairs[day_name]:
                # Check if the hour is within the range of the current day
                hour_start = current.replace(hour=hour, minute=0, second=0, microsecond=0)
                hour_end = hour_start + datetime.timedelta(hours=1)

                # Adjust based on the start and end time
                if hour_start < start < hour_end or hour_start < end < hour_end:
                    count[f"{day_name}:{hour}"] += 1
                elif hour_start >= start and hour_end <= end:
                    count[f"{day_name}:{hour}"] += 1

        # Move to the next day
        current += datetime.timedelta(days=1)

    return dict(count)

# Execute the function and print the result
result = count_day_hour_occurrences(start, end, day_hour_pairs)
print(result)
