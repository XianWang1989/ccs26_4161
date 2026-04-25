
import csv

# Test data
test = ['item1', '01', '001', 1]

# Wrap the desired item in double quotes
test[1] = f'"{test[1]}"'

# Open file in append mode
with open('file.txt', 'a', newline='') as csvfile:
    csvOut = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)

    # Write the row to the CSV file
    csvOut.writerow(test)

# To verify the output, printing to the console
print(test)  # Expected output: ['item1', '"01"', '001', 1]
