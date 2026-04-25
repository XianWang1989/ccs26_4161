
import csv

# Test data
test = ['item1', '01', '001', 1]

# Add quotes to the second item
test[1] = '"{}"'.format(test[1])

# Open the file in append mode
with open('file.txt', 'a', newline='') as f:
    csvOut = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    csvOut.writerow(test)

# Output example
print(test)
