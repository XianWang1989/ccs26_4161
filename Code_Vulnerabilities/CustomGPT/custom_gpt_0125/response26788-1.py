
import csv

reader = csv.DictReader(open("test1.csv", "r"))
allrows = list(reader)

# Extract columns that do not contain only '0's across all rows
keepcols = [c for c in allrows[0] if all(r[c] != '0' for r in allrows)]

print(keepcols)

# Correctly set fieldnames to the keepcols list
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=keepcols, extrasaction='ignore')
    writer.writeheader()  # Write the header
    writer.writerows(allrows)
