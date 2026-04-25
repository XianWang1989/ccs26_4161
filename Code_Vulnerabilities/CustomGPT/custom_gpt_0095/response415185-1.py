
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
start_date = datetime.datetime(2015, 7, 22, 17, 58, 54, 746784)
end_date = datetime.datetime(2015, 8, 30, 10, 22, 36, 363912)

def count_day_hour_pairs(day_hour_dict, start, end):
    counts = defaultdict(int)

    # Iterate through each day of the week
    for day, hours in day_hour_dict.items():
        for hour in hours:
            # Start from the next occurrence of the specific day
            current = start + datetime.timedelta(days=(7 - start.weekday() + list(day_hour_dict.keys()).index(day)) % 7)

            while current <= end:
                if current.hour == hour:
                    counts[f"{day}: {hour}"] += 1
                current += datetime.timedelta(weeks=1)  # Move to the next week

    return counts

# Count occurrences
result = count_day_hour_pairs(day_hour_pairs, start_date, end_date)

# Display results
for key, value in result.items():
    print(f"{key}: {value}")

# To count specific day-hour pair: Wednesdays at 14
def count_specific_day_hour(start, end, day, hour):
    count = 0
    current = start + datetime.timedelta(days=(7 - start.weekday() + ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'].index(day)) % 7)

    while current <= end:
        if current.hour == hour:
            count += 1
        current += datetime.timedelta(weeks=1)  # Move to next week

    return count

# Example usage for Wednesdays at 14
count_wednesday_14 = count_specific_day_hour(start_date, end_date, 'Wed', 14)
print(f"Wednesdays at 14: {count_wednesday_14}")
