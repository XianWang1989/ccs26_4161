
def count_day_hour_pairs(start, end, pairs):
    results = {}

    for day, hours in pairs.items():
        for hour in hours:
            count = count_specific_day_hour(start, end, day, hour)
            results[f"{day} at {hour}:00"] = count

    return results

# Example usage with multiple pairs
day_hour_pairs = {
    'Mon': [9, 23],
    'Thu': [12, 13, 14],
    'Tue': [11, 12, 14],
    'Wed': [11, 12, 13, 14],
    'Fri': [13],
    'Sat': [],
    'Sun': [],
}

result = count_day_hour_pairs(start_time, end_time, day_hour_pairs)
print(result)
