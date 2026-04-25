
import csv

# Read the CSV file
with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Extract columns that only contain '1's (except the first column)
keepcols = ['Title'] + [c for c in allrows[0] if all(r[c] == '1' for r in allrows)]

# Write the output to a new CSV file
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=keepcols, extrasaction='ignore')
    writer.writeheader()  # Write the header
    for row in allrows:
        # Create a new dict with only the columns to keep
        filtered_row = {col: row[col] for col in keepcols}
        writer.writerow(filtered_row)
