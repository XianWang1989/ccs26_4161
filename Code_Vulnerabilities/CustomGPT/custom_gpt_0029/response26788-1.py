
import csv

# Read the CSV file
with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Keep only columns with at least one '1'
keepcols = [c for c in allrows[0] if all(r[c] != '0' for r in allrows)]

# Write the output to a new CSV file
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=keepcols, extrasaction='ignore')
    writer.writeheader()  # Write the header
    writer.writerows(allrows)  # Write remaining rows
