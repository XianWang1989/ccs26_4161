
def count_single_day_hour(start, end, day, hour):
    count = 0
    current_time = start

    while current_time <= end:
        if current_time.strftime('%a') == day and current_time.hour == hour:
            count += 1
        current_time += timedelta(hours=1)

    return count

# Count Wednesdays at 14
count_wednesdays_14 = count_single_day_hour(start, end, 'Wed', 14)
print(f"Wednesdays at 14: {count_wednesdays_14}")
