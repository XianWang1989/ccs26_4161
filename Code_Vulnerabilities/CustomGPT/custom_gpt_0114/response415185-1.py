
from datetime import datetime, timedelta
import collections

# Define the pairs of day-hour
day_hour_pairs = {
    'Mon': [9, 23],
    'Thu': [12, 13, 14],
    'Tue': [11, 12, 14],
    'Wed': [11, 12, 13, 14],
    'Fri': [13],
    'Sat': [],
    'Sun': [],
}

# Start and end datetime
start = datetime(2015, 7, 22, 17, 58, 54, 746784)
end = datetime(2015, 8, 30, 10, 22, 36, 363912)

# Function to count hours for the defined day-hour pairs
def count_hours(start, end, day_hour_pairs):
    day_counts = collections.defaultdict(int)

    current_day = start
    while current_day <= end:
        day_name = current_day.strftime('%a')  # Get day name (Mon, Tue, ...)
        if day_name in day_hour_pairs:
            for hour in day_hour_pairs[day_name]:
                # Check if the hour falls within the start and end time
                if (current_day.hour == hour and start <= current_day <= end):
                    day_counts[(day_name, hour)] += 1

                # Increment to next hour
                next_hour = current_day.replace(hour=(hour + 1) % 24)
                while next_hour.hour == 0:  # Adjust to next day at midnight
                    next_hour += timedelta(days=1)

                # Count from start time if it's the first hour
                if hour == current_day.hour and start <= next_hour < end:
                    day_counts[(day_name, hour)] += 1

        # Move to the next day
        current_day += timedelta(days=1)

    return day_counts

# Count and display results
results = count_hours(start, end, day_hour_pairs)
for (day, hour), count in results.items():
    print(f"{day} at {hour}:00 - {count} hours")

