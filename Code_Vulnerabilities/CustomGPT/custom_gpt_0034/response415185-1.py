
import datetime
from collections import defaultdict

# Define your day-hour pairs
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

def count_day_hour_pairs(day_hour_dict, start, end):
    count = defaultdict(int)

    # Iterate through each day from start to end date
    current_date = start
    while current_date <= end:
        day_name = current_date.strftime("%a")  # Get the abbreviated name of the day
        current_hour = current_date.hour

        # Check if it's a valid day and hour in our pairs
        if day_name in day_hour_dict:
            if current_hour in day_hour_dict[day_name]:
                count[f"{day_name}: {current_hour}"] += 1

        # Move to the next hour
        current_date += datetime.timedelta(hours=1)
        # If we pass midnight, increment the day
        if current_date.hour == 0:
            current_date += datetime.timedelta(days=1)

    return count

# Count and print results
day_hour_count = count_day_hour_pairs(day_hour_pairs, start, end)
for key, value in day_hour_count.items():
    print(f"{key}: {value}")

# To count a specific pair, e.g., Wednesdays at 14
specific_count = day_hour_count.get('Wed: 14', 0)
print(f"Wednesdays at 14: {specific_count}")
