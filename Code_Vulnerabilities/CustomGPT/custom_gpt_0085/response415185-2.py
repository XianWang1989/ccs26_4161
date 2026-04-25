
def count_single_day_hour(start, end, day, hour):
    current = start
    count = 0

    while current <= end:
        if current.strftime('%a') == day and current.hour == hour:
            count += 1
        current += datetime.timedelta(hours=1)

    return count

# Example for counting Wednesdays at 14:00
wednesday_count = count_single_day_hour(start_time, end_time, 'Wed', 14)
print(f'Wednesdays at 14:00 count: {wednesday_count}')
