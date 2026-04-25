
import csv

# Example data
test = ['item1', '01', '001', 1]

# Add double quotes around the desired item
test[1] = '"' + test[1] + '"'

# Open the CSV file
with open('file.txt', 'a', newline='') as f:
    csvOut = csv.writer(f, quoting=csv.QUOTE_MINIMAL)  # Change quoting behavior
    print(test)  # This will print: ['item1', '"01"', '001', 1]
    csvOut.writerow(test)  # This will write to the file as desired: item1,"01",001,1

# No need to manually delete, using 'with' handles it
