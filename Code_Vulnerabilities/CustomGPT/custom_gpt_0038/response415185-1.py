
from datetime import datetime, timedelta

def count_specific_day_hour(start, end, day, hour):
    # Create a mapping of weekdays to their corresponding numbers
    day_mapping = {'Mon': 0, 'Tue': 1, 'Wed': 2, 'Thu': 3, 'Fri': 4, 'Sat': 5, 'Sun': 6}

    # Initialize the count
    count = 0
    current = start

    # Move to the next occurrence of the specified day
    while current <= end:
        if current.weekday() == day_mapping[day] and current.hour == hour:
            count += 1
        current += timedelta(hours=1)  # Check next hour

    return count

# Example usage
start_time = datetime(2015, 7, 22, 17, 58, 54)
end_time = datetime(2015, 8, 30, 10, 22, 36)

result = count_specific_day_hour(start_time, end_time, 'Wed', 14)
print(f"Wednesdays at 14:00 between {start_time} and {end_time}: {result}")
