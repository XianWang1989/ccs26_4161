
import csv

# Example data
test = ['item1', '01', '001', 1]

# Manually add quotes to the item as needed
test[1] = f'"{test[1]}"'

# Open the CSV file in append mode
with open('file.txt', 'a', newline='') as csvfile:
    csvOut = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
    # Write the row
    csvOut.writerow(test)

# Print the test data for verification
print(test)  # Output: ['item1', '"01"', '001', 1]
