
import csv

# Read the CSV file
with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Get columns that contain only 1s (except the first column)
keepcols = [c for c in allrows[0] if c != 'Title' and all(r[c] == '1' for r in allrows)]

# Write to the output CSV file
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=['Title'] + keepcols, extrasaction='ignore')
    writer.writeheader()  # Write the header to the output file
    for row in allrows:
        # Include only the Title and the columns we want to keep
        filtered_row = {k: row[k] for k in ['Title'] + keepcols}
        writer.writerow(filtered_row)
