
def count_specific_day_hour(start, end, day, hour):
    count = 0
    current_date = start

    while current_date <= end:
        if current_date.strftime('%a') == day and current_date.hour == hour:
            count += 1
        current_date += timedelta(days=1)

    return count

# Example usage for counting Wednesdays at hour 14
specific_count = count_specific_day_hour(start, end, 'Wed', 14)
print(f"Wednesdays at hour 14: {specific_count} occurrences")
