
from datetime import datetime, timedelta
import calendar

# Define the day-of-week-hour pairs
time_pairs = {
    'Mon': [9, 23],
    'Thu': [12, 13, 14],
    'Tue': [11, 12, 14],
    'Wed': [11, 12, 13, 14],
    'Fri': [13],
    'Sat': [],
    'Sun': [],
}

# Define the start and end datetime
start = datetime(2015, 7, 22, 17, 58, 54, 746784)
end = datetime(2015, 8, 30, 10, 22, 36, 363912)

# Function to count specific day-hour occurrences
def count_day_hour(start, end, target_day, target_hour):
    count = 0
    current = start

    while current <= end:
        if current.strftime("%a") == target_day and current.hour == target_hour:
            count += 1
        current += timedelta(hours=1)

    return count

# Example usage for "Wednesdays: 14"
day = 'Wed'
hour = 14
total_count = count_day_hour(start, end, day, hour)

print(f"Total '{day}:{hour}' occurrences between the given datetimes: {total_count}")
