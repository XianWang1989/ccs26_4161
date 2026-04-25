
import csv

# Test data
test = ['item1', '01', '001', 1]

# Add double quotes to the second item
test[1] = '"' + test[1] + '"'

# Open the file with 'a' mode to append
with open('file.txt', 'a', newline='') as file:
    csvOut = csv.writer(file, quoting=csv.QUOTE_MINIMAL)

    # Write the row
    csvOut.writerow(test)

# Print to verify
print(test)
