
import csv

# Test data
test = ['item1', '01', '001', 1]

# Add double quotes around the desired item
test[1] = '"{}"'.format(test[1])  # This keeps the internal quotes intact

# Use the CSV writer
with open('file.txt', 'a', newline='') as f:  # 'a' used for appending
    csvOut = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    csvOut.writerow(test)

# Print output to verify
print(test)  # Prints: ['item1', '"01"', '001', 1]
