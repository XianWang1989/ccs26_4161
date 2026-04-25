
def count_specific_day_hour(start, end, day, hour):
    current = start
    count = 0

    while current <= end:
        if current.strftime('%a') == day and current.hour == hour:
            count += 1
        current += datetime.timedelta(hours=1)

    return count

# Count occurrences of 'Wed: 14'
specific_count = count_specific_day_hour(start, end, 'Wed', 14)
print(f"'Wed 14' occurrences: {specific_count}")
