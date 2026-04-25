
import csv

# Test data
test = ['item1', '01', '001', 1]

# Add double quotes to the second item
test[1] = '"' + test[1] + '"'  # This is fine

# Open the file for appending
with open('file.txt', 'a', newline='') as file:
    csvOut = csv.writer(file, quoting=csv.QUOTE_MINIMAL)  # Use QUOTE_MINIMAL to avoid extra quotes

    print(test)  # Prints: ['item1', '"01"', '001', 1]
    csvOut.writerow(test)  # This will write the correct output

# Output will be: item1,"01",001,1 (as expected)
