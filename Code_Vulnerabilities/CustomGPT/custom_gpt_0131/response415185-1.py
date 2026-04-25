
import datetime
from collections import defaultdict

# Define the day-of-week-hour pairs
day_hour_pairs = {
    'Mon': [9, 23],
    'Tue': [11, 12, 14],
    'Wed': [11, 12, 13, 14],
    'Thu': [12, 13, 14],
    'Fri': [13],
    'Sat': [],
    'Sun': []
}

# Function to count the hours in the specified range for a single day-hour pair
def count_hours(start, end, day_hour_pairs):
    total_count = defaultdict(int)

    current = start
    while current <= end:
        day_name = current.strftime("%a")  # Get the day of the week (Mon, Tue, etc.)
        hour = current.hour

        if hour in day_hour_pairs.get(day_name, []):
            total_count[(day_name, hour)] += 1

        current += datetime.timedelta(hours=1)  # Increment by one hour

    return total_count

# Example usage with the specified start and end datetime
start_time = datetime.datetime(2015, 7, 22, 17, 58, 54, 746784)
end_time = datetime.datetime(2015, 8, 30, 10, 22, 36, 363912)

# Get the count of hours for the defined pairs
result = count_hours(start_time, end_time, day_hour_pairs)
print(result)
