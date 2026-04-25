
import csv

# Test "data"
test = ['item1', '01', '001', 1]

# Adding double quotes to the second item
test[1] = '"{}"'.format(test[1])

# Print the modified list
print(test)  # Output: ['item1', '"01"', '001', 1]

# Write to CSV file
with open('file.txt', 'a', newline='') as csvfile:
    csvOut = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
    csvOut.writerow(test)

# Check the contents of 'file.txt' to ensure the output is as expected
