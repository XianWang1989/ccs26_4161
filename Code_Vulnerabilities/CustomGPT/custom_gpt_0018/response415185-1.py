
from datetime import datetime, timedelta

def count_specific_day_hour(start, end, day, hour):
    count = 0
    current = start

    # Get the specific day number (0=Monday, 1=Tuesday, ..., 6=Sunday)
    day_number = {'Mon': 0, 'Tue': 1, 'Wed': 2, 'Thu': 3, 'Fri': 4, 'Sat': 5, 'Sun': 6}

    # Make sure to use the same time zone (assuming they are the same)
    while current <= end:
        # Check if current day matches
        if current.weekday() == day_number[day] and current.hour == hour:
            count += 1
        # Move to the next hour
        current += timedelta(hours=1)

    return count

# Example dates
start = datetime(2015, 7, 22, 17, 58, 54)
end = datetime(2015, 8, 30, 10, 22, 36)

# Count Wednesdays at 14
count = count_specific_day_hour(start, end, 'Wed', 14)
print(f"Count of Wednesdays at 14:00: {count}")
