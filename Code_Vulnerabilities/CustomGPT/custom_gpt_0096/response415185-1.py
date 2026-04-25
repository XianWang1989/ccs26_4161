
import datetime

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

# Define your date range
start = datetime.datetime(2015, 7, 22, 17, 58, 54, 746784)
end = datetime.datetime(2015, 8, 30, 10, 22, 36, 363912)

def count_day_hour_pairs(start, end, pairs):
    # Create a counter for each day-hour pair
    count = {day: 0 for day in pairs}

    # Iterate through each day in the date range
    current = start
    while current <= end:
        weekday = current.strftime('%a')  # Get the day of the week
        hour = current.hour                # Get the hour (24H format)

        if weekday in pairs and hour in pairs[weekday]:
            count[weekday] += 1

        # Increment to the next hour
        current += datetime.timedelta(hours=1)

    return count

# Count the day-hour occurrences
result = count_day_hour_pairs(start, end, day_hour_pairs)
print(result)
