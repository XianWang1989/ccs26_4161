
def count_single_day_hour(start, end, day, hour):
    count = 0
    current = start
    while current <= end:
        if current.strftime('%a') == day and current.hour == hour:
            count += 1
        current += datetime.timedelta(hours=1)
    return count

# Example usage for "Wednesdays: 14"
count_wednesdays_14 = count_single_day_hour(start_datetime, end_datetime, 'Wed', 14)
print(f"Wednesdays at 14: {count_wednesdays_14}")
