
import csv

# test "data"
test = ['item1', '01', '001', 1]

# Add double quotes around the desired item
test[1] = '"{}"'.format(test[1])

# Open file in append mode and use QUOTE_MINIMAL
with open('file.txt', 'a', newline='') as file:
    csvOut = csv.writer(file, quoting=csv.QUOTE_MINIMAL)

    print(test)  # Prints: ['item1', '"01"', '001', 1]
    csvOut.writerow(test)  # Write to file: item1,"01",001,1
