
import csv

# Read the CSV file
with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Identify columns to keep
keepcols = [c for c in allrows[0] if c != "Title" and any(r[c] == '1' for r in allrows)]

# Write the selected columns to a new CSV file
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=["Title"] + keepcols, extrasaction='ignore')
    writer.writeheader()  # Write header first
    for row in allrows:
        output_row = {col: row[col] for col in ["Title"] + keepcols}  # Keep only the required columns
        writer.writerow(output_row)
