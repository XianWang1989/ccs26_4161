
def count_day_hour_pairs(start, end, day_hour_pairs):
    results = {}

    # Loop through each day-hour pair
    for day, hours in day_hour_pairs.items():
        for hour in hours:
            count = count_specific_day_hour(start, end, day, hour)
            results[f"{day} at {hour}:00"] = count

    return results

# Day-hour pairs as provided
day_hour_pairs = {
    'Mon': [9, 23],
    'Thu': [12, 13, 14],
    'Tue': [11, 12, 14],
    'Wed': [11, 12, 13, 14],
    'Fri': [13],
    'Sat': [],
    'Sun': [],
}

# Count occurrences between the specified datetimes
results = count_day_hour_pairs(start, end, day_hour_pairs)

# Print the results
for pair, count in results.items():
    print(f'Number of {pair} between the dates: {count}')
