
from datetime import datetime, timedelta

# Define the day-hour pairs
day_hour_pairs = {
    'Mon': [9, 23],
    'Tue': [11, 12, 14],
    'Wed': [11, 12, 13, 14],
    'Thu': [12, 13, 14],
    'Fri': [13],
    'Sat': [],
    'Sun': [],
}

# Define the start and end datetime
start = datetime(2015, 7, 22, 17, 58, 54)
end = datetime(2015, 8, 30, 10, 22, 36)

def count_day_hour_pairs(start, end, pairs):
    count = 0

    # Iterate through each day of the week
    current = start
    while current <= end:
        # Check if the current day has hours defined
        day_name = current.strftime('%a')  # Get abbreviated name of the day (Mon, Tue, ...)
        if day_name in pairs:
            # Check hours for the current day
            for hour in pairs[day_name]:
                if current.hour == hour:
                    count += 1
        # Move to the next hour
        if current.hour == 23:
            current = current.replace(hour=0) + timedelta(days=1)
        else:
            current = current.replace(hour=current.hour + 1)

    return count

# Count the occurrences for the defined pairs
result = count_day_hour_pairs(start, end, day_hour_pairs)
print("Total occurrences:", result)
