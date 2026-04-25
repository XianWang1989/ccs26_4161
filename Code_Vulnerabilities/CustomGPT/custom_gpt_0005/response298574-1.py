
import csv

# Initial data
test = ['item1', '01', '001', 1]

# Wrap the second item with quotes correctly
test[1] = '"{}"'.format(test[1])

with open('file.txt', 'a', newline='') as file:
    csvOut = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
    csvOut.writerow(test)

# Output check
print(test)  # Should print: ['item1', '"01"', '001', 1]
