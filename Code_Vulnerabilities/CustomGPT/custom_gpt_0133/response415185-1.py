
import datetime
from collections import defaultdict

# Define the day-of-week hour pairs
day_hour_pairs = {
    'Mon': [9, 23],
    'Thu': [12, 13, 14],
    'Tue': [11, 12, 14],
    'Wed': [11, 12, 13, 14],
    'Fri': [13],
    'Sat': [],
    'Sun': [],
}

# Define your datetime range
start = datetime.datetime(2015, 7, 22, 17, 58, 54)
end = datetime.datetime(2015, 8, 30, 10, 22, 36)

def count_day_hour_pairs(start, end, day_hour_pairs):
    # Initialize a dictionary to hold the count of hours for each day-of-week
    counts = defaultdict(int)

    # Adjust the start datetime to the next weekday
    current = start
    while current <= end:
        day_of_week = current.strftime('%a')  # Get the day of the week

        if day_of_week in day_hour_pairs:
            for hour in day_hour_pairs[day_of_week]:
                # Check if the current hour falls within the start and end range
                if current.hour == hour:
                    counts[(day_of_week, hour)] += 1

        # Move to the next hour
        current += datetime.timedelta(hours=1)

    return counts

# Call the function and print results
result = count_day_hour_pairs(start, end, day_hour_pairs)

# Pretty print the results
for (day, hour), count in result.items():
    print(f"{day}: {hour} -> Count: {count}")
