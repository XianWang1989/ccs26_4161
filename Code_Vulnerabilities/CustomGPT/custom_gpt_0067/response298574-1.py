
import csv

# Test data
test = ['item1', '01', '001', 1]

# Add quotes around the second item
test[1] = '"' + test[1] + '"'

# Open the file and create a CSV writer
with open('file.txt', 'a', newline='') as file:
    csvOut = csv.writer(file, quoting=csv.QUOTE_MINIMAL)

    # Print the modified list for reference
    print(test)  # prints: ['item1', '"01"', '001', 1]

    # Write to the CSV file
    csvOut.writerow(test)  # Expected: item1,"01",001,1
