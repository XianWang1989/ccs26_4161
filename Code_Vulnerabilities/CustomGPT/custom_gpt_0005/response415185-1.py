
import datetime

def count_day_hour_pairs(start, end, day_hour_pairs):
    # Initialize a dictionary to store count results
    count_results = {day: 0 for day in day_hour_pairs}

    # Iterate over each day in the day_hour_pairs
    for day, hours in day_hour_pairs.items():
        # Calculate the start of the first occurrence of the given day
        first_occurrence = start + datetime.timedelta(days=(7 + day_index(day) - start.weekday()) % 7)

        # Loop through the hours to count valid occurrences
        for hour in hours:
            current_time = first_occurrence.replace(hour=hour, minute=0, second=0, microsecond=0)

            while current_time <= end:
                if start <= current_time <= end:
                    count_results[day] += 1
                current_time += datetime.timedelta(weeks=1)

    return count_results

def day_index(day):
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    return days.index(day)

# Example usage
start = datetime.datetime(2015, 7, 22, 17, 58, 54, 746784)
end = datetime.datetime(2015, 8, 30, 10, 22, 36, 363912)

day_hour_pairs = {
    'Mon': [9, 23],
    'Thu': [12, 13, 14],
    'Tue': [11, 12, 14],
    'Wed': [11, 12, 13, 14],
    'Fri': [13],
    'Sat': [],
    'Sun': [],
}

results = count_day_hour_pairs(start, end, day_hour_pairs)
print(results)
