
def count_specific_day_hour(start, end, day, hour):
    count = 0
    current = start

    while current <= end:
        if current.strftime('%a') == day and current.hour == hour:
            count += 1
        current += datetime.timedelta(hours=1)

    return count

# Count "Wednesdays at 14"
count_wednesday_14 = count_specific_day_hour(start_dt, end_dt, 'Wed', 14)
print(f'Wednesdays at 14: {count_wednesday_14}')
