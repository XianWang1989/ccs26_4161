
def count_day_hour_pairs(start, end, pairs):
    results = {}

    for day, hours in pairs.items():
        for hour in hours:
            results[(day, hour)] = count_day_hour(start, end, day, hour)

    return results

# Example pairs
pairs = {
    'Mon': [9, 23],
    'Thu': [12, 13, 14],
    'Tue': [11, 12, 14],
    'Wed': [11, 12, 13, 14],
    'Fri': [13],
    'Sat': [],
    'Sun': [],
}

# Count occurrences for all pairs
occurrences = count_day_hour_pairs(start, end, pairs)
print(occurrences)
