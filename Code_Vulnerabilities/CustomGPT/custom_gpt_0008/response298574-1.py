
import csv

# Test data
test = ['item1', '01', '001', 1]

# Wrap the second item with double quotes without altering the CSV behavior
test[1] = '"{}"'.format(test[1])

# Open CSV file for appending
with open('file.txt', 'a', newline='') as file:
    csvOut = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
    csvOut.writerow(test)

# Print output for verification
print(test)
