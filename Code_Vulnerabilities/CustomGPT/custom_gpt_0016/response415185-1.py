
import datetime
from collections import defaultdict

# Define the day-of-week-hour pairs
day_hour_pairs = {
    'Mon': [9, 23],
    'Tue': [11, 12, 14],
    'Wed': [11, 12, 13, 14],
    'Thu': [12, 13, 14],
    'Fri': [13],
    'Sat': [],
    'Sun': [],
}

# Function to count specific day-hour combinations between two datetimes
def count_day_hour_pairs(start_dt, end_dt, day_hour_pairs):
    count = defaultdict(int)

    # Iterate through each day in the range
    current_dt = start_dt
    while current_dt <= end_dt:
        day_name = current_dt.strftime('%a')  # Get the day name (e.g., 'Mon')
        current_hour = current_dt.hour  # Get the current hour

        # If the current day has specific hours
        if day_name in day_hour_pairs:
            # Check if the current hour is in the list of hours for that day
            if current_hour in day_hour_pairs[day_name]:
                count[day_name] += 1

        # Move to the next hour, incrementing the current time
        current_dt += datetime.timedelta(hours=1)

    return dict(count)

# Example start and end datetimes
start = datetime.datetime(2015, 7, 22, 17, 58, 54)
end = datetime.datetime(2015, 8, 30, 10, 22, 36)

# Count the day-hour pairs
result = count_day_hour_pairs(start, end, day_hour_pairs)
print(result)
