
import datetime
from collections import defaultdict

# Define the dictionary with day-of-week-hour pairs
schedule = {
    'Mon': [9, 23],
    'Thu': [12, 13, 14],
    'Tue': [11, 12, 14],
    'Wed': [11, 12, 13, 14],
    'Fri': [13],
    'Sat': [],
    'Sun': []
}

# Define the start and end datetime
start = datetime.datetime(2015, 7, 22, 17, 58, 54, 746784)
end = datetime.datetime(2015, 8, 30, 10, 22, 36, 363912)

def count_day_hour_pairs(schedule, start, end):
    count = defaultdict(int)

    current = start
    while current <= end:
        # Get the day of the week
        day_name = current.strftime('%a')  # 'Mon', 'Tue', etc.

        # Check if this day is in the schedule
        if day_name in schedule:
            # Check the hours for this day
            for hour in schedule[day_name]:
                if current.hour == hour:
                    count[(day_name, hour)] += 1

        # Move to the next hour
        current += datetime.timedelta(hours=1)

    return dict(count)

# Run the function
result = count_day_hour_pairs(schedule, start, end)
print(result)
