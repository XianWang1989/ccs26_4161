
import csv

# Test data
test = ['item1', '01', '001', 1]

# Wrap the desired item in quotes, but handle them correctly
test[1] = '"{}"'.format(test[1])

# Open CSV file for appending
with open('file.txt', 'a', newline='') as f:
    csvOut = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    csvOut.writerow(test)

# Confirm the output
print(test)
