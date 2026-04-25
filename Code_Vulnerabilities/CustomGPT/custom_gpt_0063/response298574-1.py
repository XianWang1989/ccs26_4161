
import csv

# Test data
test = ['item1', '01', '001', 1]

# Manually add quotes to the second item
test[1] = '"01"'

# Open the output file in append mode
with open('file.txt', 'a', newline='') as f:
    csvOut = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
    csvOut.writerow(test)

# Print output for verification
print(test)
