
import csv

# Reading the CSV file
with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Extracting columns with at least one '1'
keepcols = [c for c in allrows[0] if any(r[c] == '1' for r in allrows)]

# Writing to the output file
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=keepcols, extrasaction='ignore')
    writer.writeheader()  # Write the header
    writer.writerows(allrows)

print(keepcols)  # To see the extracted columns
