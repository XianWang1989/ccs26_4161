
import csv

# Test data
test = ['item1', '01', '001', 1]

# Manually format the second item to be quoted
test[1] = '"{}"'.format(test[1])

# Open the CSV file for appending
with open('file.txt', 'a', newline='') as file:
    csvOut = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
    # Write the row
    csvOut.writerow(test)

# Print the output to verify
print(test)
