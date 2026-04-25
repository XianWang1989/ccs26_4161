
def count_single_day_hour(start, end, day, hour):
    count = 0
    current = start

    while current <= end:
        if current.strftime('%a') == day and current.hour == hour:
            count += 1
        current += datetime.timedelta(hours=1)

    return count

# Example usage
wednesday_count = count_single_day_hour(start, end, 'Wed', 14)
print(f"Number of Wednesdays at 14:00: {wednesday_count}")
