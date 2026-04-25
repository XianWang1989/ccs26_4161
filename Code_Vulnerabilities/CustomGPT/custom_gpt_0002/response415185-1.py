
from datetime import datetime, timedelta

def count_day_hour_pairs(start, end, day_hour_pairs):
    # Initialize a dictionary to hold counts for each day-hour pair
    count_dict = {day: 0 for day in day_hour_pairs}

    # Iterate through each day and its available hours
    current = start
    while current <= end:
        day_name = current.strftime('%a')  # Get day name in abbreviated form

        if day_name in day_hour_pairs:
            for hour in day_hour_pairs[day_name]:
                # Check if the current hour matches the day's hours
                if current.hour == hour:
                    count_dict[day_name] += 1

        current += timedelta(hours=1)  # Move to the next hour

    return count_dict

# Example usage
day_hour_pairs = {
    'Mon': [9, 23],
    'Thu': [12, 13, 14],
    'Tue': [11, 12, 14],
    'Wed': [11, 12, 13, 14],
    'Fri': [13],
    'Sat': [],
    'Sun': [],
}

start = datetime(2015, 7, 22, 17, 58, 54)
end = datetime(2015, 8, 30, 10, 22, 36)

counts = count_day_hour_pairs(start, end, day_hour_pairs)
print(counts)
