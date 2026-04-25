
import csv

# Read the input CSV file
with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Determine which columns to keep (those that contain '1')
keepcols = [c for c in allrows[0] if any(r[c] == '1' for r in allrows)]

# Write the output CSV file with only the selected columns
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=keepcols)
    writer.writeheader()  # Write the header
    for row in allrows:
        # Create a new row dict with only the columns we want to keep
        filtered_row = {c: row[c] for c in keepcols}
        writer.writerow(filtered_row)  # Write the filtered row
