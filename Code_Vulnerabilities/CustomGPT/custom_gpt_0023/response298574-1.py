
import csv

# Test data
test = ['item1', '01', '001', 1]

# Wrap the desired item in quotes
test[1] = '"{}"'.format(test[1])

# Open a file for appending
with open('file.txt', 'a', newline='') as file:
    csvOut = csv.writer(file, quoting=csv.QUOTE_MINIMAL)  # Adjust quoting as needed
    csvOut.writerow(test)

# Output will be: item1,"01",001,1 without any extra quotes
