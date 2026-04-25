
import csv

# Read the CSV file
with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Identify columns that contain only 0s or 1s, excluding '0' columns
keepcols = [c for c in reader.fieldnames if any(r[c] == '1' for r in allrows)]

# Write the selected columns to a new CSV file
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=['Title'] + keepcols, extrasaction='ignore')
    writer.writeheader()  # Write the header
    for row in allrows:
        # Create a new row with only the selected columns
        new_row = {col: row[col] for col in ['Title'] + keepcols}
        writer.writerow(new_row)
