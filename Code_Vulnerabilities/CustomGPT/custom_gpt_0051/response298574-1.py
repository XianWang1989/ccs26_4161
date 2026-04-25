
import csv

# Sample data
test = ['item1', '01', '001', 1]

# Adding quotes to the second item
test[1] = f'"{test[1]}"'

# Writing to a CSV file
with open('file.txt', 'a', newline='') as csvfile:
    csvOut = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
    csvOut.writerow(test)

# To verify, you can also print the list
print(test)  # Output: ['item1', '"01"', '001', 1]
