
def count_single_day_hour(start, end, day, hour):
    count = 0
    current_day = start
    while current_day <= end:
        if current_day.strftime('%a') == day and current_day.hour == hour:
            count += 1
        current_day += datetime.timedelta(hours=1)
    return count

# Example usage for Wednesdays at hour 14
count_wed_14 = count_single_day_hour(start_time, end_time, 'Wed', 14)
print(f"Wednesdays at 14: {count_wed_14}")
