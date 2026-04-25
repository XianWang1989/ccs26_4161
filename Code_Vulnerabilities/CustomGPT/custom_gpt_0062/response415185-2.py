
def count_specific_day_hour(start, end, day, hour):
    count = 0
    current = start

    while current <= end:
        if current.strftime("%a") == day and current.hour == hour:
            count += 1
        current += timedelta(hours=1)

    return count

# Count occurrences of "Wednesdays: 14"
specific_count = count_specific_day_hour(start, end, 'Wed', 14)
print(specific_count)
