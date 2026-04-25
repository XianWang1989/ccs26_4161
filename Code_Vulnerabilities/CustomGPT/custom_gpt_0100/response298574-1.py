
import csv

# Test data
test = ['item1', '01', '001', 1]

# Preprocess the data to add quotes without causing double-quoting issues
test[1] = '"{}"'.format(test[1])  # Add quotes to the second item

with open('file.txt', 'a', newline='') as file:
    csvOut = csv.writer(file, quoting=csv.QUOTE_MINIMAL)  # Use QUOTE_MINIMAL
    csvOut.writerow(test)

# Verify output by printing
print(test)
