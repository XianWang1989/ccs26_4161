
from datetime import datetime, timedelta

# Define your day-hour mapping
day_hour_pairs = {
    'Mon': [9, 23],
    'Thu': [12, 13, 14],
    'Tue': [11, 12, 14],
    'Wed': [11, 12, 13, 14],
    'Fri': [13],
    'Sat': [],
    'Sun': [],
}

# Function to count hours for a specific day-hour pair
def count_day_hour(start, end, day, hour):
    count = 0
    current = start

    while current <= end:
        if current.strftime('%a') == day and current.hour == hour:
            count += 1
        current += timedelta(hours=1)

    return count

# Define start and end datetime
start_date = datetime(2015, 7, 22, 17, 58, 54, 746784)
end_date = datetime(2015, 8, 30, 10, 22, 36, 363912)

# Count Wednesdays at 14:00
wednesday_count = count_day_hour(start_date, end_date, 'Wed', 14)
print(f"There are {wednesday_count} Wednesdays at 14:00 between the two dates.")
