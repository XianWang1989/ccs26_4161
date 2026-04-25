
import csv

# Test data
test = ['item1', '01', '001', 1]

# Manually add quotes around the desired item
test[1] = '"{}"'.format(test[1])

# Open the file in append mode
with open('file.txt', 'a', newline='') as file:
    csvOut = csv.writer(file, quoting=csv.QUOTE_MINIMAL, quotechar='"')
    csvOut.writerow(test)

# Print output for verification
print(test)  # Output: ['item1', '"01"', '001', 1]
