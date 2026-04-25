
def count_specific_day_hour(start, end, day, hour):
    count = 0
    current_date = start

    while current_date <= end:
        if current_date.strftime('%a') == day and current_date.hour == hour:
            count += 1

        # Move to the next hour or day
        if current_date.hour == 23:
            current_date += datetime.timedelta(days=1)
            current_date = current_date.replace(hour=0)
        else:
            current_date += datetime.timedelta(hours=1)

    return count

# Example usage for "Wednesday: 14"
specific_count = count_specific_day_hour(start_time, end_time, 'Wed', 14)
print(f"Wednesdays at 14: {specific_count}")
