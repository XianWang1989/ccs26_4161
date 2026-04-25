
import datetime
from collections import defaultdict

# Define the day-of-week-hour pairs
day_hour_pairs = {
    'Mon': [9, 23],
    'Thu': [12, 13, 14],
    'Tue': [11, 12, 14],
    'Wed': [11, 12, 13, 14],
    'Fri': [13],
    'Sat': [],
    'Sun': [],
}

def count_day_hour_pairs(start_dt, end_dt):
    # Convert the start and end datetime to the same timezone if necessary
    current_dt = start_dt
    count = defaultdict(int)

    # Create a set of the target day-hour pairs 
    target_pairs = {day: set(hours) for day, hours in day_hour_pairs.items()}

    # Iterate through all dates in the range
    while current_dt <= end_dt:
        # Get the day of the week and hour
        day_name = current_dt.strftime('%a')
        hour = current_dt.hour

        # Check if the current hour is in the target pairs for that day
        if day_name in target_pairs and hour in target_pairs[day_name]:
            count[(day_name, hour)] += 1

        # Move to the next hour
        current_dt += datetime.timedelta(hours=1)

    return count

# Define the two datetimes
start = datetime.datetime(2015, 7, 22, 17, 58, 54, 746784)
end = datetime.datetime(2015, 8, 30, 10, 22, 36, 363912)

# Execute the function
result = count_day_hour_pairs(start, end)

# Print the result
for key, value in result.items():
    print(f"{key}: {value}")
