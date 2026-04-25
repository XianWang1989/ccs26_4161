
import datetime
import numpy as np

# Define your day-of-week-hour pairs
dow_hours = {
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

def count_dow_hour_pairs(start, end, dow_hours):
    count = {day: 0 for day in dow_hours.keys()}  # Initialize counts

    # Loop through each day in the date range
    current = start
    while current <= end:
        weekday = current.strftime('%A')  # Get the day of the week
        hour = current.hour  # Get the hour of the current datetime

        # Check if the current weekday and hour match any of the pairs
        if weekday in dow_hours and hour in dow_hours[weekday]:
            count[weekday] += 1

        # Move to the next hour
        current += datetime.timedelta(hours=1)

    return count

# Call the function
result = count_dow_hour_pairs(start, end, dow_hours)
print(result)

# Focusing on a simpler problem: Counting Wednesdays at 14
def count_specific_dow_hour(start, end, day, hour):
    count = 0
    current = start
    while current <= end:
        if current.strftime('%A') == day and current.hour == hour:
            count += 1
        current += datetime.timedelta(hours=1)
    return count

# Example for counting Wednesdays at 14
wednesday_count = count_specific_dow_hour(start, end, 'Wednesday', 14)
print(f"Wednesdays at 14: {wednesday_count}")
