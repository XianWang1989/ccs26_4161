
import datetime
from collections import defaultdict

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

def count_occurrences(start, end, day_hour_pairs):
    count = defaultdict(int)

    # Loop through each day and hour pair
    for day, hours in day_hour_pairs.items():
        for hour in hours:
            # Start from the first occurrence of the day in the range
            current_date = start
            while current_date < end:
                # Move to the next week, if it's not the correct day
                while current_date.weekday() != list(day_hour_pairs.keys()).index(day):
                    current_date += datetime.timedelta(days=1)

                # Check if the hour is correct
                if current_date.hour == hour and current_date >= start and current_date <= end:
                    count[(day, hour)] += 1

                # Move to the next occurrence of the same day
                current_date += datetime.timedelta(days=7)

    return count

# Count occurrences
occurrences = count_occurrences(start, end, day_hour_pairs)

# Output the result for Wednesday at 14:00
print(f"Wednesdays at 14:00 count: {occurrences.get(('Wed', 14), 0)}")
