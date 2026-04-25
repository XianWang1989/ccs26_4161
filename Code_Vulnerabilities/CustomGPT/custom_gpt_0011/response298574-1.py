
import csv

# Example data
test = ['item1', '01', '001', 1]

# Quote only the specific item
test[1] = '"{}"'.format(test[1])

# Open the CSV file for writing
with open('file.txt', 'a', newline='') as csvfile:
    csvOut = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
    print(test)  # This will print: ['item1', '"01"', '001', 1]
    csvOut.writerow(test)  # This will write: item1,"01",001,1

# Note: Ensure to close the file if not using 'with' context
