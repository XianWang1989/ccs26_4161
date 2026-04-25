
import csv

# Test data
test = ['item1', '01', '001', 1]

# Add double quotes to a specific item
test[1] = '"{}"'.format(test[1])

# Open the CSV file in append mode
with open('file.txt', 'a', newline='') as f:
    csvOut = csv.writer(f, quoting=csv.QUOTE_MINIMAL, quotechar='"')
    print(test)  # Output: ['item1', '"01"', '001', 1]
    csvOut.writerow(test)  # Output to file: item1,"01",001,1
