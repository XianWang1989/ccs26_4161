
import csv

# Prepare the test data
test = ['item1', '01', '001', 1]

# Manually add quotes to the second element
test[1] = '"{}"'.format(test[1])

# Open the file for writing
with open('file.txt', 'a', newline='') as f:
    csvOut = csv.writer(f, quoting=csv.QUOTE_MINIMAL, quotechar='"', escapechar='\\')
    csvOut.writerow(test)

# Verify output
print(test)  # This should print: ['item1', '"01"', '001', 1]
