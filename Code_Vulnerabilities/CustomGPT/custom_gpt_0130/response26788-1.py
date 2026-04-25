
import csv

# Read the CSV file
with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Identify columns to keep
keepcols = [c for c in allrows[0] if all(r[c] == '1' for r in allrows)]

# Create an output file with only the selected columns
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=keepcols, extrasaction='ignore')
    writer.writeheader()  # Write the header
    for row in allrows:
        # Create a new row with only the columns to keep
        filtered_row = {c: row[c] for c in keepcols}
        writer.writerow(filtered_row)
