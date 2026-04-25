
def count_specific_pair(start, end, day, hour):
    count = 0
    current = start
    while current <= end:
        if current.strftime('%a') == day and current.hour == hour:
            count += 1
        current += datetime.timedelta(hours=1)
    return count

# Count for Wednesdays at 14
wednesday_14_count = count_specific_pair(start, end, 'Wed', 14)
print(f"Wednesdays at 14: {wednesday_14_count}")
