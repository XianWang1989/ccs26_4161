
def count_specific_day_hour(start, end, day, hour):
    count = 0
    current_datetime = start

    while current_datetime <= end:
        if current_datetime.strftime('%a') == day and current_datetime.hour == hour:
            count += 1
        current_datetime += datetime.timedelta(hours=1)

    return count

# Count Wednesdays at 14
wednesday_14_count = count_specific_day_hour(start, end, 'Wed', 14)

print(f"Wednesdays at 14: {wednesday_14_count}")
