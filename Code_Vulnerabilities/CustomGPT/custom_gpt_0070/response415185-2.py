
def count_single_day_hour(start, end, day, hour):
    count = 0
    current = start

    while current <= end:
        if current.strftime('%a') == day and current.hour == hour:
            count += 1
        current += timedelta(hours=1)

    return count

# Count "Wednesdays: 14"
wednesday_14_count = count_single_day_hour(start, end, 'Wed', 14)
print(f'Wednesdays at 14:00 count: {wednesday_14_count}')
