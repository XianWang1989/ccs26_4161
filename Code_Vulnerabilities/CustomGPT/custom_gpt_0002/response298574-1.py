
import csv

# Test data
test = ['item1', '01', '001', 1]

# Modify the second item to have double quotes
test[1] = '"{}"'.format(test[1])

# Open the file for appending
with open('file.txt', 'a', newline='') as file:
    csvOut = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
    csvOut.writerow(test)

# This will write: item1,"01",001,1
