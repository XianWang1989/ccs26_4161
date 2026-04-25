
def count_specific_day_hour(start, end, day, hour):
    count = 0
    current = start
    while current <= end:
        if current.strftime('%a') == day and current.hour == hour:
            count += 1
        current += datetime.timedelta(hours=1)
    return count

# Count specific case: "Wednesdays: 14"
count_weds_14 = count_specific_day_hour(start, end, 'Wed', 14)
print(f"Wednesdays: 14 -> Count: {count_weds_14}")
