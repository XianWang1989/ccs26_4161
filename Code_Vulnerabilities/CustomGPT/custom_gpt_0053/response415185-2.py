
def count_specific_day_hour(start, end, day, hour):
    count = 0
    current = start

    while current <= end:
        if current.strftime('%a') == day and current.hour == hour:
            count += 1
        current += datetime.timedelta(hours=1)

    return count

# Count Wednesdays at 14:00
wednesday_count = count_specific_day_hour(start_time, end_time, 'Wed', 14)
print(f"Wednesdays at 14:00: {wednesday_count} occurrences")
