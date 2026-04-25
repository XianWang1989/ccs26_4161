
import csv

# Sample data
test = ['item1', '01', '001', 1]

# Manually add quotes around specific items
test[1] = '"{}"'.format(test[1])  # This adds quotes only to '01'

print(test)  # Expected output: ['item1', '"01"', '001', 1]

# Create a CSV writer object
with open('file.txt', 'a', newline='') as file:
    csvOut = csv.writer(file, quoting=csv.QUOTE_MINIMAL)  # Use QUOTE_MINIMAL

    # Write the row to the CSV file
    csvOut.writerow(test)

print("Data written to file.txt")
