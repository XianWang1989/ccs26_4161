
def count_specific_day_hour(day, hour, start, end):
    count = 0
    current = start

    while current <= end:
        if current.strftime('%a') == day and current.hour == hour:
            count += 1
        current += datetime.timedelta(minutes=1)

    return count

# Example use for Wednesday at 14
specific_count = count_specific_day_hour('Wed', 14, start, end)
print(specific_count)
