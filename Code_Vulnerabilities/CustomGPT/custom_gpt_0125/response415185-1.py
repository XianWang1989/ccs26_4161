
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

def count_hours(start, end, day_hour_pairs):
    count_results = defaultdict(int)

    # Iterate through each datetime between the start and end
    current = start
    while current <= end:
        day_of_week = current.strftime('%a')  # Get day of week abbreviation (Mon, Tue, ...)
        hour = current.hour

        # Check if the current hour is in the pairs for that day
        if hour in day_hour_pairs.get(day_of_week, []):
            count_results[(day_of_week, hour)] += 1

        # Move to the next hour
        current += datetime.timedelta(hours=1)

    return dict(count_results)

# Example Usage
start_time = datetime.datetime(2015, 7, 22, 17, 58, 54)
end_time = datetime.datetime(2015, 8, 30, 10, 22, 36)

# Count hours based on the defined pairs
results = count_hours(start_time, end_time, day_hour_pairs)

# Output results
for (day, hour), count in results.items():
    print(f"{day} {hour:02d}: {count}")

# Simplified problem: Count "Wednesdays: 14"
def count_single_day_hour(start, end, day, hour):
    count = 0
    current = start
    while current <= end:
        if current.strftime('%a') == day and current.hour == hour:
            count += 1
        current += datetime.timedelta(hours=1)
    return count

# Count "Wednesdays: 14"
single_result = count_single_day_hour(start_time, end_time, 'Wed', 14)
print(f"Wednesdays at 14:00: {single_result}")
