
import csv

# Sample data
test = ['item1', '01', '001', 1]

# Add double quotes around the second item
test[1] = '"{}"'.format(test[1])

# Open a file for appending
with open('file.txt', 'a', newline='') as f:
    csvOut = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    print(test)  # Prints: ['item1', '"01"', '001', 1]
    csvOut.writerow(test)  # Output will be: item1,"01",001,1
