
def count_specific_day_hour(start, end, day, hour):
    current = start
    count = 0

    while current <= end:
        if current.strftime("%a") == day and current.hour == hour:
            count += 1
        current += datetime.timedelta(days=1)

    return count

# Count Wednesdays at 14
count_wednesday_14 = count_specific_day_hour(start, end, 'Wed', 14)
print(f"Wednesdays at 14: {count_wednesday_14}")
