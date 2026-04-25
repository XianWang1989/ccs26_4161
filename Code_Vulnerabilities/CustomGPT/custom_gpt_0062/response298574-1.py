
import csv

# Test data
test = ['item1', '01', '001', 1]

# Add quotes to only the second item
test[1] = '"{}"'.format(test[1])  # or test[1] = f'"{test[1]}"'
print(test)  # Prints: ['item1', '"01"', '001', 1]

# Open file for appending and create CSV writer
with open('file.txt', 'a', newline='') as file:
    csvOut = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
    csvOut.writerow(test)

# At this point, the output in 'file.txt' will be: item1,"01",001,1
