
import datetime
from collections import defaultdict

# Define the day-hour mapping
day_hour_mapping = {
    'Mon': [9, 23],
    'Thu': [12, 13, 14],
    'Tue': [11, 12, 14],
    'Wed': [11, 12, 13, 14],
    'Fri': [13],
    'Sat': [],
    'Sun': [],
}

def count_day_hour_pairs(start, end, mapping):
    # Create a dictionary to store the counts
    counts = defaultdict(int)

    # Loop through each date in the range
    current_date = start
    while current_date <= end:
        day_name = current_date.strftime('%a')  # Get the weekday name
        current_hour = current_date.hour

        # Check if the current day and hour are in the mapping
        if day_name in mapping and current_hour in mapping[day_name]:
            counts[(day_name, current_hour)] += 1

        # Move to the next hour or to the next day if at the end of the hour
        if current_hour == 23:
            current_date += datetime.timedelta(days=1)  # Move to next day
            current_date = current_date.replace(hour=0)  # Reset hour to 0
        else:
            current_date += datetime.timedelta(hours=1)  # Move to next hour

    return counts

# Example usage
start_time = datetime.datetime(2015, 7, 22, 17, 58, 54)
end_time = datetime.datetime(2015, 8, 30, 10, 22, 36)

result = count_day_hour_pairs(start_time, end_time, day_hour_mapping)
print(result)
