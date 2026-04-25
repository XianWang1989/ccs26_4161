
import csv

# Test data
test = ['item1', '01', '001', 1]

# Update the item with quotes for display, without affecting the CSV output
test[1] = '"01"'

# Open the CSV file for appending
with open('file.txt', 'a', newline='') as f:
    csvOut = csv.writer(f, quoting=csv.QUOTE_MINIMAL)  # Use minimal quoting

    # Print the modified list
    print(test)

    # Write the row to the CSV file
    csvOut.writerow(test)
