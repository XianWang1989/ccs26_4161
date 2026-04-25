
from datetime import datetime, timedelta

# Function to count specific hours on a specific day of the week
def count_specific_day_hour(start, end, day, hour):
    count = 0
    current_date = start

    while current_date <= end:
        if current_date.strftime('%a') == day and current_date.hour == hour:
            count += 1
        current_date += timedelta(hours=1)

    return count

# Function to count all specified day-hour pairs in a given range
def count_day_hour_pairs(start, end, day_hour_pairs):
    counts = {}
    current_date = start

    while current_date <= end:
        day_name = current_date.strftime('%a')
        if day_name in day_hour_pairs:
            for hour in day_hour_pairs[day_name]:
                if current_date.hour == hour:
                    key = f"{day_name}:{hour}"
                    counts[key] = counts.get(key, 0) + 1
        current_date += timedelta(hours=1)

    return counts

# Example usage
start_time = datetime(2015, 7, 22, 17, 58, 54)
end_time = datetime(2015, 8, 30, 10, 22, 36)

# Defining day-hour pairs
day_hour_pairs = {
    'Mon': [9, 23],
    'Thu': [12, 13, 14],
    'Tue': [11, 12, 14],
    'Wed': [11, 12, 13, 14],
    'Fri': [13],
    'Sat': [],
    'Sun': [],
}

# Counting all specified pairs
counts = count_day_hour_pairs(start_time, end_time, day_hour_pairs)

print("Counts of day-hour pairs:", counts)

# Counting specific case: Wednesdays at 14
wednesday_14_count = count_specific_day_hour(start_time, end_time, 'Wed', 14)
print("Count of Wednesdays at 14:", wednesday_14_count)
