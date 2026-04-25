
import datetime
from collections import defaultdict

# Define the day-hour pairs
day_hour_pairs = {
    'Mon': [9, 23],
    'Tue': [11, 12, 14],
    'Wed': [11, 12, 13, 14],
    'Thu': [12, 13, 14],
    'Fri': [13],
    'Sat': [],
    'Sun': [],
}

def count_day_hour_pairs(start_dt, end_dt, day_hour_pairs):
    # Create a default dictionary to hold counts for each day-hour pair
    counts = defaultdict(int)

    # Generate a range of dates between start_dt and end_dt
    current_date = start_dt
    while current_date <= end_dt:
        day_name = current_date.strftime("%a")  # Get the day name (e.g., 'Mon', 'Tue')
        if day_name in day_hour_pairs:
            # Check hours for the specific day
            for hour in day_hour_pairs[day_name]:
                if current_date.hour < hour:
                    # Count the current hour only if it falls within the range
                    if start_dt.date() != current_date.date() or start_dt.hour <= hour:
                        counts[(day_name, hour)] += 1
                elif current_date.hour == hour:
                    # If current hour equals the hour, count this occurrence
                    if current_date >= start_dt and current_date <= end_dt:
                        counts[(day_name, hour)] += 1
                # If it's after the hour, check if the following hours fall within the range
                elif current_date.hour > hour and (current_date.date() != end_dt.date() or current_date.hour < end_dt.hour):
                    counts[(day_name, hour)] += 1

        # Move to the next day
        current_date += datetime.timedelta(days=1)

    return counts

# Define start and end dates
start = datetime.datetime(2015, 7, 22, 17, 58, 54, 746784)
end = datetime.datetime(2015, 8, 30, 10, 22, 36, 363912)

# Get counts
counts = count_day_hour_pairs(start, end, day_hour_pairs)

# Print the results
for pair, count in counts.items():
    print(f"{pair}: {count}")
