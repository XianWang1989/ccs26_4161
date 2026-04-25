
import csv

# Test data
test = ['item1', '01', '001', 1]

# Add double quotes to the second item
test[1] = '"{}"'.format(test[1])  # This will ensure single quotes are added

with open('file.txt', 'a', newline='') as file:  # Using with statement for better resource management
    csvOut = csv.writer(file, quoting=csv.QUOTE_MINIMAL)  # Change quoting option
    print(test)  # Output will be: ['item1', '"01"', '001', 1]
    csvOut.writerow(test)  # Writes: item1,"01",001,1
