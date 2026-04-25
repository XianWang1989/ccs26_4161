
import csv

# Test data
test = ['item1', '01', '001', 1]

# Adding quotes to the second item
test[1] = '"{}"'.format(test[1])

# Writing to the CSV file
with open('file.txt', 'a', newline='') as file:
    csvOut = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
    csvOut.writerow(test)

# Output example to console
print(test)
