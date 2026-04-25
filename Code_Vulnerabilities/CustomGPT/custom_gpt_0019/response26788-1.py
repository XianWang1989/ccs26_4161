
import csv

# Read the CSV file
with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Identify columns to keep (those with at least one '1')
keepcols = [
    c for c in allrows[0] 
    if c != "Title" and any(r[c] == '1' for r in allrows)
]

# Write to the output CSV file
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=["Title"] + keepcols, extrasaction='ignore')
    writer.writeheader()  # Write the header
    for row in allrows:
        writer.writerow({k: row[k] for k in keepcols + ["Title"]})

print("Columns with at least one '1' have been extracted.")
