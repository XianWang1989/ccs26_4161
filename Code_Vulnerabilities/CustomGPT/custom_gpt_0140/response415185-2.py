
def count_specific_hour(start, end, day, hour):
    count = 0
    current = start

    while current <= end:
        if current.strftime('%a') == day and current.hour == hour:
            count += 1
        current += datetime.timedelta(hours=1)

    return count

# Count specific hours for 'Wed' at 14
wednesday_14_count = count_specific_hour(start, end, 'Wed', 14)
print(f'Total Wednesdays at 14:00: {wednesday_14_count}')
