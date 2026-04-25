
import csv

# Test data
test = ['item1', '01', '001', 1]

# Wrap the second item in quotes
test[1] = '"{}"'.format(test[1])  # Adding double quotes
print(test)  # Prints: ['item1', '"01"', '001', 1]

# Write the data to a CSV file
with open('file.txt', 'a', newline='') as f:
    csvOut = csv.writer(f, quoting=csv.QUOTE_MINIMAL)  # Only quote fields containing special characters
    csvOut.writerow(test)

# The output file will now contain: item1,"01",001,1
