
import csv

# Test data
test = ['item1', '01', '001', 1]

# Open the file in append mode
with open('file.txt', 'a', newline='') as f:
    csvOut = csv.writer(f, quoting=csv.QUOTE_MINIMAL)  # Customize quoting behavior
    test[1] = '"'+test[1]+'"'  # Add quotes around the desired item

    print(test)  # prints: ['item1', '"01"', '001', 1]
    csvOut.writerow(test)  # writes: item1,"01",001,1
