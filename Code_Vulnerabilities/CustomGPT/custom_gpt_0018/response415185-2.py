
def count_day_hour_pairs(start, end, day_hour_dict):
    results = {}

    for day, hours in day_hour_dict.items():
        for hour in hours:
            count = count_specific_day_hour(start, end, day, hour)
            results[f"{day} at {hour}:00"] = count

    return results

# Your day-hour pairs dictionary
day_hour_pairs = {
    'Mon': [9, 23],
    'Thu': [12, 13, 14],
    'Tue': [11, 12, 14],
    'Wed': [11, 12, 13, 14],
    'Fri': [13],
    'Sat': [],
    'Sun': [],
}

# Get counts for all pairs
all_counts = count_day_hour_pairs(start, end, day_hour_pairs)
print(all_counts)
