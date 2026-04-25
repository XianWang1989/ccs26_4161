
import csv

# Test data
test = ['item1','01','001',1]

# Prepare the writer
with open('file.txt', 'a', newline='') as csvfile:
    csvOut = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)  # Use minimal quoting

    # Update the second item with quotes for writing
    test[1] = f'"{test[1]}"'
    print(test)  # Prints: ['item1', '"01"', '001', 1]

    # Write the row to the CSV file
    csvOut.writerow(test)

# Check the output in 'file.txt'
