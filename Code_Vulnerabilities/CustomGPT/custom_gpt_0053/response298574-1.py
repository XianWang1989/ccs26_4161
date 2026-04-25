
import csv

# Sample data
test = ['item1', '01', '001', 1]

# Modify the second item to have quotes around it
test[1] = '"{}"'.format(test[1])

# Open the output file in append mode
with open('file.txt', 'a', newline='') as csvfile:
    csvOut = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
    csvOut.writerow(test)

# Check the result by printing
print('Written output:', test)
