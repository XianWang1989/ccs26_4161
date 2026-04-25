
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

def count_day_hour_pairs(start, end, day_hour_pairs):
    current = start
    count = defaultdict(int)

    # Loop through each day until the end date
    while current < end:
        day_name = current.strftime('%a')  # Get the day of the week
        if day_name in day_hour_pairs:
            current_hour = current.hour
            if current_hour in day_hour_pairs[day_name]:
                count[(day_name, current_hour)] += 1
        current += datetime.timedelta(hours=1)  # Move to the next hour

    return count

# Example usage
start = datetime.datetime(2015, 7, 22, 17, 58, 54)
end = datetime.datetime(2015, 8, 30, 10, 22, 36)

result = count_day_hour_pairs(start, end, day_hour_pairs)
for k, v in result.items():
    print(f"{k}: {v}")

# Function to count specific day-hour pair
def count_specific_day_hour(start, end, day, hour):
    current = start
    count = 0

    while current < end:
        if current.strftime('%a') == day and current.hour == hour:
            count += 1
        current += datetime.timedelta(hours=1)

    return count

# Count for Wednesdays at 14:00
wed_14_count = count_specific_day_hour(start, end, 'Wed', 14)
print(f"Wednesdays at 14:00: {wed_14_count}")
