
import csv

# Sample data
test = ['item1', '01', '001', 1]

# Open the file in append mode
with open('file.txt', 'a', newline='') as csvfile:
    csvOut = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)  # Use minimal quoting

    # Modify the specific item
    test[1] = '"01"'  # Add double quotes directly around the string

    # Write the row to the CSV file
    csvOut.writerow(test)

# Output confirmation
print(test)  # This will show: ['item1', '"01"', '001', 1]
