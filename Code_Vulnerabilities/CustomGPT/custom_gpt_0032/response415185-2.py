
def count_all_day_hour_pairs(start, end, day_hour_pairs):
    counts = {}

    for day, hours in day_hour_pairs.items():
        for hour in hours:
            counts[(day, hour)] = count_specific_day_hour(start, end, day, hour)

    return counts

# Define the pairs
day_hour_data = {
    'Mon': [9, 23],
    'Thu': [12, 13, 14],
    'Tue': [11, 12, 14],
    'Wed': [11, 12, 13, 14],
    'Fri': [13],
    'Sat': [],
    'Sun': [],
}

# Count pairs
result = count_all_day_hour_pairs(start_time, end_time, day_hour_data)

# Display results
for (day, hour), count in result.items():
    print(f"Count of {day} at {hour}:00 is: {count}")
