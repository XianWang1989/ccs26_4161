
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

# Define the start and end datetimes
start = datetime.datetime(2015, 7, 22, 17, 58, 54, 746784)
end = datetime.datetime(2015, 8, 30, 10, 22, 36, 363912)

def count_hours(day_hour_pairs, start, end):
    # Initialize the count dictionary
    hour_counts = {day: 0 for day in day_hour_pairs}

    # Iterate from start to end date, week by week
    current_date = start
    while current_date <= end:
        day_name = current_date.strftime("%a")  # Get the abbreviated day name

        if day_name in day_hour_pairs:
            for hour in day_hour_pairs[day_name]:
                hour_start = current_date.replace(hour=hour, minute=0, second=0, microsecond=0)
                hour_end = current_date.replace(hour=hour + 1, minute=0, second=0, microsecond=0)

                # Check if the hour is within the start and end datetime
                if (hour_start < end) and (hour_end > start):
                    hour_counts[day_name] += 1

        # Move to the next day
        current_date += datetime.timedelta(days=1)

    return hour_counts

# Count the hours
results = count_hours(day_hour_pairs, start, end)

# Print results
for day, count in results.items():
    print(f"{day}: {count}")
