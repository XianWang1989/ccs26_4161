
import csv

# Test data
test = ['item1', '01', '001', 1]

# Format the second item to include quotes without extra quotes
test[1] = '"{}"'.format(test[1])

# Check printed output
print(test)  # prints: ['item1', '"01"', '001', 1]

# Writing to CSV
with open('file.txt', 'a', newline='') as file:
    csvOut = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
    csvOut.writerow(test)

# This will write: item1,"01",001,1
