
def count_specific_day_hour(start, end, day_name, hour):
    count = 0
    current = start
    while current <= end:
        if current.strftime('%a') == day_name and current.hour == hour:
            count += 1
        current += datetime.timedelta(hours=1)
    return count

# Count occurrences of 'Wednesday' at 14:00
wednesday_count = count_specific_day_hour(start, end, 'Wed', 14)
print(f"Wednesdays at 14:00 count: {wednesday_count}")
