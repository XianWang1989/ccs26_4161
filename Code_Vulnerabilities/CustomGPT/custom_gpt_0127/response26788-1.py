
import csv

# Reading the CSV file
with open("test1.csv", "r") as file:
    reader = csv.DictReader(file)
    allrows = list(reader)

# Extracting columns with at least one '1'
keepcols = [c for c in allrows[0] if any(r[c] == '1' for r in allrows)]

# Writing filtered rows to a new CSV file
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=keepcols, extrasaction='ignore')
    writer.writeheader()
    for row in allrows:
        filtered_row = {c: row[c] for c in keepcols}  # Keep only the selected columns
        writer.writerow(filtered_row)
