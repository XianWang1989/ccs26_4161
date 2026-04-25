
def count_specific_day_hour(start, end, day, hour):
    current = start
    count = 0

    while current <= end:
        if current.strftime('%a') == day and current.hour == hour:
            count += 1
        current += timedelta(hours=1)

    return count

# Count occurrences for Wednesdays at 14
wednesday_14_count = count_specific_day_hour(start, end, 'Wed', 14)
print(f"Wednesdays at 14: {wednesday_14_count} occurrences")
