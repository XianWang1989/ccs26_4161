
import datetime
from collections import defaultdict

def count_day_hour_pairs(start, end, schedule):
    day_counts = defaultdict(int)

    # Iterating through each day in the date range
    current = start
    while current <= end:
        weekday = current.strftime('%a')  # Get the abbreviated weekday name
        if weekday in schedule:
            # Check hours for the current day
            for hour in schedule[weekday]:
                # Count if the hour is within the range for that day
                if current.hour <= hour < (current.hour + 1) or current.hour < hour:
                    if current <= end:
                        day_counts[(weekday, hour)] += 1
        current += datetime.timedelta(hours=1)  # Increment by one hour

    return day_counts

# Example schedule
schedule = {
    'Mon': [9, 23],
    'Thu': [12, 13, 14],
    'Tue': [11, 12, 14],
    'Wed': [11, 12, 13, 14],
    'Fri': [13],
    'Sat': [],
    'Sun': [],
}

# Example start and end datetimes
start = datetime.datetime(2015, 7, 22, 17, 58, 54)
end = datetime.datetime(2015, 8, 30, 10, 22, 36)

# Count pairs
counts = count_day_hour_pairs(start, end, schedule)

# Display results
for key, count in counts.items():
    print(f"{key}: {count}")
