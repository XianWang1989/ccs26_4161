
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

# Define the start and end datetime objects
start = datetime.datetime(2015, 7, 22, 17, 58, 54, 746784)
end = datetime.datetime(2015, 8, 30, 10, 22, 36, 363912)

def count_day_hour_pairs(start, end, pairs):
    # Create a dictionary to hold the counts of each day-hour pair
    counts = defaultdict(int)

    # Start from the beginning of the week containing the start date
    current = start
    current_weekday = current.weekday()  # Monday is 0, Sunday is 6
    start_week_start = current - datetime.timedelta(days=current_weekday)

    # Iterate through weeks until we reach the end date
    while current_week_start <= end:
        for day, hours in pairs.items():
            day_index = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'].index(day)
            day_date = start_week_start + datetime.timedelta(days=day_index)

            # Check if this day is within the start and end dates
            if start <= day_date <= end:
                # Count the valid hours within the given range
                for hour in hours:
                    # Create the specific datetime for that hour
                    hourly_datetime = day_date.replace(hour=hour, minute=0, second=0, microsecond=0)
                    # Count if valid within the range
                    if start <= hourly_datetime <= end:
                        counts[(day, hour)] += 1

        # Move to the next week
        start_week_start += datetime.timedelta(weeks=1)

    return counts

# Call the function and print the results
result = count_day_hour_pairs(start, end, day_hour_pairs)
for (day, hour), count in result.items():
    print(f"{count} occurrences of {day}: {hour}")
