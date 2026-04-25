
import datetime

# Sample day-hour pairs
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
start = datetime.datetime(2015, 7, 22, 17, 58, 54)
end = datetime.datetime(2015, 8, 30, 10, 22, 36)

def count_wednesdays_hour(start, end, hour):
    # Initialize the count for Wednesdays at specified hour
    count = 0
    # Iterate from start to end date
    current = start
    while current <= end:
        if current.weekday() == 2 and current.hour == hour:  # 2 corresponds to Wednesday
            count += 1
        current += datetime.timedelta(hours=1)  # Increment by one hour
    return count

# Example for counting Wednesdays at 14
wednesday_hour = 14
wednesday_count = count_wednesdays_hour(start, end, wednesday_hour)

print(f'Number of Wednesdays at {wednesday_hour}:00 = {wednesday_count}')

# Extend to count for all pairs
def count_pairs(start, end, pairs):
    results = {}
    for day, hours in pairs.items():
        results[day] = {}
        for hour in hours:
            results[day][hour] = count_wednesdays_hour(start, end, hour)  # Call the counting function
    return results

# Count for all day-hour pairs
total_counts = count_pairs(start, end, day_hour_pairs)
print(total_counts)
