
import csv

# Test data
test = ['item1', '01', '001', 1]

# Adding quotes to the second item
test[1] = '"'+test[1]+'"'

# Using QUOTE_MINIMAL to control how quotes are handled
with open('file.txt', 'a', newline='') as f:  # 'a' for appending
    csvOut = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    csvOut.writerow(test)

# Printing for reference
print(test)  # This will print: ['item1', '"01"', '001', 1]
