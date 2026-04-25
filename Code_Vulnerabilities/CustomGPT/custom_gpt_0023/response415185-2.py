
def count_single_day_hour(start, end, day, hour):
    count = 0
    current = start.replace(minute=0, second=0, microsecond=0)

    while current <= end:
        if current.strftime('%a') == day and current.hour == hour:
            count += 1
        current += timedelta(hours=1)

    return count

# Count Wednesdays at 14:00
count_wed_14 = count_single_day_hour(start_dt, end_dt, 'Wed', 14)
print(f"Wednesdays at 14:00: {count_wed_14}")
