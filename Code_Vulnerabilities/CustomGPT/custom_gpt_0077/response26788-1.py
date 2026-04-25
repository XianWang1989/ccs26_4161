
import csv

# Read the CSV file
with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Identify columns that contain at least one '1'
keepcols = [c for c in allrows[0] if any(r[c] == '1' for r in allrows)]

# Write the filtered columns to a new CSV file
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=keepcols, extrasaction='ignore')
    writer.writeheader()
    for row in allrows:
        filtered_row = {k: row[k] for k in keepcols}
        writer.writerow(filtered_row)
