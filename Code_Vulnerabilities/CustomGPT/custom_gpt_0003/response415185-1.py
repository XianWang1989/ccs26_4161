
import datetime
from collections import defaultdict

# Day-hour mapping provided in the question
day_hour_pairs = {
    'Mon': [9, 23],
    'Tue': [11, 12, 14],
    'Wed': [11, 12, 13, 14],
    'Thu': [12, 13, 14],
    'Fri': [13],
    'Sat': [],
    'Sun': [],
}

def count_day_hour_pairs(start, end, day_hour_mapping):
    current = start
    count = defaultdict(int)

    while current <= end:
        day_name = current.strftime("%a")  # Get the day of the week (Mon, Tue, ...)
        hour = current.hour

        if day_name in day_hour_mapping and hour in day_hour_mapping[day_name]:
            count[(day_name, hour)] += 1

        # Move to the next hour
        if current.hour == 23:
            current = current.replace(hour=0) + datetime.timedelta(days=1)
        else:
            current = current.replace(hour=current.hour + 1)

    return count

# Example usage
start = datetime.datetime(2015, 7, 22, 17, 58, 54, 746784)
end = datetime.datetime(2015, 8, 30, 10, 22, 36, 363912)

count_results = count_day_hour_pairs(start, end, day_hour_pairs)

# Display the results
for (day, hour), occurrences in count_results.items():
    print(f"{occurrences} occurrences of {day} at {hour}:00")
