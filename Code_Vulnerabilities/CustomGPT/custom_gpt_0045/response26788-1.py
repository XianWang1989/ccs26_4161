
import csv

# Read the CSV file
with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Identify which columns to keep
keepcols = [c for c in allrows[0] if all(r[c] == '1' for r in allrows)]

# Output the columns with '1's
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=keepcols, extrasaction='ignore')
    writer.writeheader()  # Write the headers
    for row in allrows:
        # Filter the row to include only the columns in keepcols
        filtered_row = {c: row[c] for c in keepcols}
        writer.writerow(filtered_row)
