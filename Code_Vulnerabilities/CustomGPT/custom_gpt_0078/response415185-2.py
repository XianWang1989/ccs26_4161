
from datetime import datetime, timedelta

def count_day_hour_pairs(start, end, day_hour_pairs):
    results = {}

    for day, hours in day_hour_pairs.items():
        total_count = 0
        for hour in hours:
            total_count += count_day_hour(start, end, day, hour)
        results[day] = total_count

    return results

# Given day-hour pairs
day_hour_pairs = {
    'Mon': [9, 23],
    'Thu': [12, 13, 14],
    'Tue': [11, 12, 14],
    'Wed': [11, 12, 13, 14],
    'Fri': [13],
    'Sat': [],
    'Sun': [],
}

# Example usage
start = datetime(2015, 7, 22, 17, 58, 54, 746784)
end = datetime(2015, 8, 30, 10, 22, 36, 363912)
results = count_day_hour_pairs(start, end, day_hour_pairs)

print("Occurrences between the two dates:")
for day, count in results.items():
    print(f"{day}: {count}")
