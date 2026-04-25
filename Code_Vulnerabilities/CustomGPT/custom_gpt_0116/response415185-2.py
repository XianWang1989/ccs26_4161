
def count_specific_day_hour(start, end, day, hour):
    weekday_map = {'Mon': 0, 'Tue': 1, 'Wed': 2, 'Thu': 3, 'Fri': 4, 'Sat': 5, 'Sun': 6}

    count = 0
    current = start

    while current <= end:
        if current.weekday() == weekday_map[day] and current.hour == hour:
            count += 1
        current += timedelta(hours=1)  # Move to the next hour

    return count

# Example usage
wednesday_14_count = count_specific_day_hour(start, end, 'Wed', 14)
print(f"Wednesdays at 14: {wednesday_14_count}")
