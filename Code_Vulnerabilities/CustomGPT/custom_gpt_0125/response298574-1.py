
import csv

# Test "data"
test = ['item1','01','001',1]

# Modify the second item to include quotes
test[1] = '"{}"'.format(test[1])

# Open the file in append mode
with open('file.txt', 'a', newline='') as f:
    csv_out = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    csv_out.writerow(test)

# Print the modified list
print(test)
# Expected output: ['item1', '"01"', '001', 1]
