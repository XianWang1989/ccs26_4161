
import csv

# Test data
test = ['item1', '01', '001', 1]

# Add double quotes to the specific item
test[1] = '"{}"'.format(test[1])

with open('file.txt', 'a', newline='') as file:
    csvOut = csv.writer(file, quoting=csv.QUOTE_MINIMAL)  # Use minimal quoting
    print(test)  # Output: ['item1', '"01"', '001', 1]
    csvOut.writerow(test)  # Writes: item1,"01",001,1
