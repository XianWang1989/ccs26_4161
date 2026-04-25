
def count_all_day_hour_occurrences(start, end, schedule):
    # Dictionary to hold the counts
    counts = {day: 0 for day in schedule}

    # Loop through all hours in the date range
    current = start.replace(minute=0, second=0, microsecond=0)

    while current <= end:
        day_name = current.strftime('%a')
        hour = current.hour

        # Check if the current hour is in the scheduled hours for that day
        if day_name in schedule and hour in schedule[day_name]:
            counts[day_name] += 1

        # Move to the next hour
        current += datetime.timedelta(hours=1)

    return counts

# Schedule of day-hour pairs
schedule = {
    'Mon': [9, 23],
    'Thu': [12, 13, 14],
    'Tue': [11, 12, 14],
    'Wed': [11, 12, 13, 14],
    'Fri': [13],
    'Sat': [],
    'Sun': [],
}

# Count occurrences for all pairs
total_counts = count_all_day_hour_occurrences(start_time, end_time, schedule)
print("Occurrences for each day-hour pair:")
for day, count in total_counts.items():
    print(f"{day}: {count}")
