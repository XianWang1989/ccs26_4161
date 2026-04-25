
import csv

# Example data with quotes
test = ['item1', '01', '001', 1]

# Add quotes to the second item
test[1] = '"' + test[1] + '"'

# Open the output file with 'a' mode to append data
with open('file.txt', 'a', newline='') as f:
    csvOut = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    csvOut.writerow(test)

# To verify the written output
print(test)
