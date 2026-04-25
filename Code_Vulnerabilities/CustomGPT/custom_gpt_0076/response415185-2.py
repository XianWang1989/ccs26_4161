
def count_specific_day_hour(start, end, day, hour):
    count = 0
    current_date = start

    while current_date <= end:
        if current_date.strftime('%a') == day and current_date.hour == hour:
            count += 1
        current_date += timedelta(hours=1)

    return count

# Count Wednesdays at 14
wednesday_14_count = count_specific_day_hour(start_datetime, end_datetime, 'Wed', 14)
print(f"Count of Wednesdays at 14: {wednesday_14_count}")
