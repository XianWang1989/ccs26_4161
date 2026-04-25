
from datetime import datetime, timedelta

def count_all_day_hour_pairs(start, end, day_hour_dict):
    results = {}

    for day, hours in day_hour_dict.items():
        for hour in hours:
            count = count_day_hour(start, end, day, hour)
            results[f"{day}: {hour}"] = count

    return results

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

start_datetime = datetime(2015, 7, 22, 17, 58, 54)
end_datetime = datetime(2015, 8, 30, 10, 22, 36)

results = count_all_day_hour_pairs(start_datetime, end_datetime, day_hour_pairs)

for key, value in results.items():
    print(f"Occurrences of {key} between {start_datetime} and {end_datetime}: {value}")
