
import csv

# Test data
test = ['item1', '01', '001', 1]

# Wrap the specific field with quotes
test[1] = '"{}"'.format(test[1])  # Wrap '01' with quotes

# Open the CSV file with 'a' for append mode
with open('file.txt', 'a', newline='') as file:
    csvOut = csv.writer(file, quoting=csv.QUOTE_MINIMAL)

    # Write the row to the CSV
    csvOut.writerow(test)

# Print the modified test to confirm
print(test)  # This will output: ['item1', '"01"', '001', 1]
