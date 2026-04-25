
import csv

# Initialize test data
test = ['item1', '01', '001', 1]

# Add double quotes around the second item
test[1] = f'"{test[1]}"'

# Open the CSV file in append mode
with open('file.txt', 'a', newline='') as file:
    csvOut = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC, escapechar='\\')
    csvOut.writerow(test)

# Print to verify
print(test)  # Should output: ['item1', '"01"', '001', 1]
