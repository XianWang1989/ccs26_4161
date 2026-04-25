
def count_specific_day_hour(start, end, day, hour):
    count = 0
    current_date = start

    while current_date <= end:
        if current_date.strftime('%a') == day and current_date.hour == hour:
            count += 1
        current_date += datetime.timedelta(hours=1)

    return count

# Count how many Wednesdays at hour 14 between start and end
wednesdays_at_14 = count_specific_day_hour(start, end, 'Wed', 14)
print(f'Wednesdays at 14: {wednesdays_at_14}')
