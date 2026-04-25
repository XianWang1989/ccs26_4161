
import datetime
from collections import defaultdict

# Function to count occurrences of day-hour pairs
def count_day_hour_pairs(start, end, day_hour_pairs):
    # Create a dictionary to hold the counts
    count_results = defaultdict(int)

    # Iterate through all days from start to end
    current = start
    while current <= end:
        # Get the day of the week in the format required
        day_name = current.strftime('%a')  # 'Mon', 'Tue', etc.

        # Check if the current day has associated hours
        if day_name in day_hour_pairs:
            for hour in day_hour_pairs[day_name]:
                # Check if the current hour matches
                if current.hour == hour:
                    count_results[(day_name, hour)] += 1

        # Move to the next hour
        current += datetime.timedelta(hours=1)

    return dict(count_results)

# Example usage
day_hour_pairs = {
    'Mon': [9, 23],
    'Tue': [11, 12, 14],
    'Wed': [11, 12, 13, 14],
    'Thu': [12, 13, 14],
    'Fri': [13],
    'Sat': [],
    'Sun': [],
}

start = datetime.datetime(2015, 7, 22, 17, 58, 54)
end = datetime.datetime(2015, 8, 30, 10, 22, 36)

result = count_day_hour_pairs(start, end, day_hour_pairs)

# Display results
for day_hour, count in result.items():
    print(f"{day_hour}: {count}")
