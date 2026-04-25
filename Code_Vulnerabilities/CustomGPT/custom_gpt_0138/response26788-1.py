
import csv

# Open the input CSV file
with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Extract column names where all entries are not '0'
keepcols = [c for c in allrows[0] if any(r[c] == '1' for r in allrows)]

# Open the output CSV file
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=keepcols, extrasaction='ignore')
    writer.writeheader()  # Write the header row
    writer.writerows([{c: r[c] for c in keepcols} for r in allrows])  # Write filtered rows
