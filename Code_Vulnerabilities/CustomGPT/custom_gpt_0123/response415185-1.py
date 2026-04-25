
import datetime
from collections import defaultdict

# Define the day-of-week-hour pairs
dow_hours = {
    'Mon': [9, 23],
    'Thu': [12, 13, 14],
    'Tue': [11, 12, 14],
    'Wed': [11, 12, 13, 14],
    'Fri': [13],
    'Sat': [],
    'Sun': [],
}

# Define start and end datetime objects
start = datetime.datetime(2015, 7, 22, 17, 58, 54, 746784)
end = datetime.datetime(2015, 8, 30, 10, 22, 36, 363912)

def count_dow_hour_pairs(dow_hours, start, end):
    current = start
    occurrences = defaultdict(int)

    # Loop through the dates
    while current <= end:
        day_name = current.strftime('%a')  # Get the day of the week
        if day_name in dow_hours:
            for hour in dow_hours[day_name]:
                # Count if the hour occurs in the current day
                if current.hour == hour and current >= start and current <= end:
                    occurrences[(day_name, hour)] += 1

        # Move to the next hour
        current += datetime.timedelta(hours=1)

    return occurrences

# Run the function and print the results
result = count_dow_hour_pairs(dow_hours, start, end)
for pair, count in result.items():
    print(f"{pair}: {count}")
