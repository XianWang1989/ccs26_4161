
import csv

# Test data
test = ['item1', '01', '001', 1]

# Wrap the second item in quotes
test[1] = '"{}"'.format(test[1])

# Printing the modified list
print(test)  # Prints: ['item1', '"01"', '001', 1]

# Open the output file and write
with open('file.txt', 'a', newline='') as file:  # 'a' used for keeping past results
    csvOut = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
    csvOut.writerow(test)

# The output in 'file.txt' will be: item1,"01",001,1
