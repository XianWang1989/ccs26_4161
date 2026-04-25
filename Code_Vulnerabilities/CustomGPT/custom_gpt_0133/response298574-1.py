
import csv

# Test data
test = ['item1', '01', '001', 1]

# Adding quotes to the second item
test[1] = f'"{test[1]}"'

# Open the CSV file in append mode and create a CSV writer
with open('file.txt', 'a', newline='') as file:
    csvOut = csv.writer(file, quoting=csv.QUOTE_MINIMAL)

    print(test)  # prints: ['item1', '"01"', '001', 1]

    # Write the row to the CSV file
    csvOut.writerow(test)

# File will now contain: item1,"01",001,1
