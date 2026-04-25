
import csv

# Test data
test = ['item1', '01', '001', 1]

# Adjust the value with quotes
test[1] = '"{}"'.format(test[1])

# Open the file for appending
with open('file.txt', 'a', newline='') as csvfile:
    csvOut = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
    csvOut.writerow(test)

# Output verification
print(test)
