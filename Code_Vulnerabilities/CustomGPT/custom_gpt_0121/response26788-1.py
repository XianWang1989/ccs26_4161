
import csv

# Read the CSV file
with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Identify columns to keep
keepcols = ['Title'] + [c for c in allrows[0] if any(r[c] == '1' for r in allrows)]

# Write the output CSV file
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=keepcols, extrasaction='ignore')
    writer.writeheader()  # Write the header
    for row in allrows:
        # Write only the columns we want to keep
        filtered_row = {key: row[key] for key in keepcols}
        writer.writerow(filtered_row)
