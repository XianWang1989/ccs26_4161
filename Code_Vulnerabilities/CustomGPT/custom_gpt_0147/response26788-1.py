
import csv

# Read the CSV file
with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Identify columns to keep (those with at least one '1')
keepcols = ['Title']  # Always include the first column 'Title'
for col in allrows[0].keys():
    if col != 'Title' and any(r[col] == '1' for r in allrows):
        keepcols.append(col)

# Write the filtered rows to the output CSV
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=keepcols, extrasaction='ignore')
    writer.writeheader()
    for row in allrows:
        # Create a new row with only the kept columns
        filtered_row = {col: row[col] for col in keepcols}
        writer.writerow(filtered_row)
