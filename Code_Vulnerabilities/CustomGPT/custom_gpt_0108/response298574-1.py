
import csv

# Test data
test = ['item1', '01', '001', 1]

# Add quotes to the string item
test[1] = '"'+test[1]+'"'

# Open the file in append mode
with open('file.txt', 'a', newline='') as file:
    csvOut = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
    print(test)  # Prints: ['item1', '"01"', '001', 1]
    csvOut.writerow(test)  # Writes: item1,"01",001,1
