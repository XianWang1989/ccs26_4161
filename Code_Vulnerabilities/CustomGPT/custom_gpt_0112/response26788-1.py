
import csv

# Read the CSV file
with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Identify columns with at least one '1'
keepcols = [c for c in allrows[0] if any(r[c] == '1' for r in allrows)]

# Write the filtered columns into a new CSV file
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=keepcols, extrasaction='ignore')
    writer.writeheader()  # Write the header
    for row in allrows:
        # Filter the row to include only the columns in keepcols
        filtered_row = {c: row[c] for c in keepcols}
        writer.writerow(filtered_row)
