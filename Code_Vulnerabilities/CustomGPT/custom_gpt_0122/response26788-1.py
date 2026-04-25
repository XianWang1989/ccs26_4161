
import csv

# Load the CSV file
with open("test1.csv", "r") as file:
    reader = csv.DictReader(file)
    allrows = list(reader)

# Find columns to keep
keepcols = [c for c in allrows[0] if all(r[c] != '0' for r in allrows if r[c] != '')]

# Prepare to write to output CSV
with open("output1.csv", "w", newline='') as output_file:
    writer = csv.DictWriter(output_file, fieldnames=keepcols, extrasaction='ignore')
    writer.writeheader()  # Write the header
    writer.writerows(allrows)

print("Extracted columns with 1's:", keepcols)
