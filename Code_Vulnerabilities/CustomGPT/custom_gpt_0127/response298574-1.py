
import csv

# Sample data
test = ['item1', '01', '001', 1]

# Adding quotes to a specific item
test[1] = '"{}"'.format(test[1])

# Open the file in append mode
with open('file.txt', 'a', newline='') as file:
    csvOut = csv.writer(file, quoting=csv.QUOTE_MINIMAL, escapechar='\\')
    csvOut.writerow(test)

# Print for verification
print(test)  # Output: ['item1', '"01"', '001', 1]
