
import csv

# Open the CSV file for reading
with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Determine which columns to keep (only those containing '1')
keepcols = ['Title'] + [c for c in allrows[0] if all(r[c] == '1' for r in allrows)]

# Open the output CSV file for writing
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=keepcols, extrasaction='ignore')
    writer.writeheader()  # Write the header to the output file
    # Write only the rows containing the kept columns
    for row in allrows:
        filtered_row = {key: row[key] for key in keepcols}
        writer.writerow(filtered_row)
