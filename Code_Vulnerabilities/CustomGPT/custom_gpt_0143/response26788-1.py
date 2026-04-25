
import csv

# Read the input CSV file
with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Extract columns that contain only 1s (excluding the first column)
keepcols = [c for c in allrows[0] if all(r[c] == '1' for r in allrows)]

# Write to the output CSV file with the selected columns
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=['Title'] + keepcols, extrasaction='ignore')
    writer.writeheader()
    for row in allrows:
        # Create a new row containing only the selected columns
        filtered_row = {col: row[col] for col in ['Title'] + keepcols}
        writer.writerow(filtered_row)
