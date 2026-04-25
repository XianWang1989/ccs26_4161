
import csv

# Test data
test = ['item1', '01', '001', 1]

# Add double quotes around the second item
test[1] = '"{}"'.format(test[1])

# Print the modified list
print(test)  # Output: ['item1', '"01"', '001', 1]

# Write to CSV
with open('file.txt', 'a', newline='') as csvfile:
    csvOut = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
    csvOut.writerow(test)

# The output in file.txt will be: item1,"01",001,1
