
def count_specific_day_hour(start, end, day, hour):
    current = start
    count = 0

    while current <= end:
        if current.strftime('%a') == day and current.hour == hour:
            count += 1
        current += datetime.timedelta(hours=1)

    return count

# Example count for 'Wed: 14'
wednesday_count = count_specific_day_hour(start, end, 'Wed', 14)
print(f"Wednesdays at 14:00 - Count: {wednesday_count}")
