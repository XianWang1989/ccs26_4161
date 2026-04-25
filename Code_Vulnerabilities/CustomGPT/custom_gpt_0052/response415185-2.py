
def count_specific_day_hour(day, hour, start, end):
    count = 0
    current = start

    while current <= end:
        if current.strftime('%a') == day and current.hour == hour:
            count += 1
        current += timedelta(hours=1)

    return count

wednesday_14_count = count_specific_day_hour('Wed', 14, start, end)
print(f"Wednesdays at 14: {wednesday_14_count}")
