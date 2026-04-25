
import csv

test = ['item1', '01', '001', 1]
test[1] = '\"' + test[1] + '\"'

with open('file.txt', 'a', newline='') as f:
    csvOut = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
    csvOut.writerow(test)

print(test)
