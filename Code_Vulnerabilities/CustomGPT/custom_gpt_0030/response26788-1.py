
import csv

# Read the CSV file
with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Identify columns to keep
keepcols = [c for c in allrows[0] if all(r[c] == '1' for r in allrows)]

# Prepare to write to the output CSV file
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=keepcols, extrasaction='ignore')
    writer.writeheader()  # Write the header first
    for row in allrows:
        # Filter out the columns we want to keep
        filtered_row = {c: row[c] for c in keepcols}
        writer.writerow(filtered_row)

print("Columns with 1's have been extracted to output1.csv.")
