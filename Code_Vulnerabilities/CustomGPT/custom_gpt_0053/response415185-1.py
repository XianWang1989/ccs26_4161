
import datetime
from collections import defaultdict

# Define the day-of-week-hour pairs
schedule = {
    'Mon': [9, 23],
    'Thu': [12, 13, 14],
    'Tue': [11, 12, 14],
    'Wed': [11, 12, 13, 14],
    'Fri': [13],
    'Sat': [],
    'Sun': [],
}

def count_hours_between(start, end, schedule):
    current = start
    count_dict = defaultdict(int)

    # Iterate through each day between start and end
    while current <= end:
        day_name = current.strftime('%a')  # Get the abbreviated weekday name
        hour = current.hour

        # Check if the current hour is in the day's allowed hours
        if hour in schedule.get(day_name, []):
            count_dict[day_name] += 1

        # Move to the next hour
        current += datetime.timedelta(hours=1)

    return count_dict

# Example datetime objects
start_time = datetime.datetime(2015, 7, 22, 17, 58, 54)
end_time = datetime.datetime(2015, 8, 30, 10, 22, 36)

# Count hours for the specified schedule
result = count_hours_between(start_time, end_time, schedule)

# Print the result
for day, count in result.items():
    print(f"{day}: {count} hours")
