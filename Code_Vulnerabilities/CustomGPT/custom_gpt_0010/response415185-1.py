
import datetime
from dateutil.relativedelta import relativedelta

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
start = datetime.datetime(2015, 7, 22, 17, 58, 54, 746784)
end = datetime.datetime(2015, 8, 30, 10, 22, 36, 363912)

def count_day_hour_pairs(day_hour_dict, start, end):
    count_dict = {}

    current = start
    while current <= end:
        # Get the weekday as a number (0=Mon, 6=Sun)
        weekday = current.strftime('%a')  # e.g., 'Mon', 'Tue', etc.

        if weekday in day_hour_dict:
            # Check each hour for that weekday
            for hour in day_hour_dict[weekday]:
                if current.hour == hour:
                    # Increment the count for this pair
                    count_dict[weekday] = count_dict.get(weekday, 0) + 1

        # Move to the next hour
        current += datetime.timedelta(hours=1)

    return count_dict

# Execute the counting
result = count_day_hour_pairs(day_hour_pairs, start, end)
print(result)
