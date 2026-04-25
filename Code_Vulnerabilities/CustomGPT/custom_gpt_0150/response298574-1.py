
import csv

# Original test data
test = ['item1', '01', '001', 1]

# Add double quotes to a single item in the list
test[1] = '"{}"'.format(test[1])

with open('file.txt', 'a', newline='') as f:
    csvOut = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    csvOut.writerow(test)

# Print the output for verification
print(test)
