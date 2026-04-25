import csv

# Prepare your data
test = ['item1', '01', '001', 1]

# Open the file with quoting set properly
with open('file.txt', 'a', newline='') as f:
    csvOut = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    csvOut.writerow(test)
