
import csv

# Sample data
test = ['item1', '01', '001', 1]

# Add double quotes to the specific item
test[1] = f'"{test[1]}"'

# Open the CSV file and write the data
with open('file.txt', 'a', newline='') as csvfile:
    csvOut = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
    csvOut.writerow(test)

# Print the output for verification
print(test)  # ['item1', '"01"', '001', 1]
