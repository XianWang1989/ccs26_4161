
import csv

# Open the CSV file and read the data
with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Identify columns where all rows have '1's (excluding the first column)
keepcols = [c for c in allrows[0] if c != 'Title' and all(r[c] == '1' for r in allrows)]

# Write the output to a new CSV file with the filtered columns
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=['Title'] + keepcols, extrasaction='ignore')
    writer.writeheader()  # Write the headers first
    for row in allrows:
        # Create a new row to include only the keepcols
        new_row = {col: row[col] for col in ['Title'] + keepcols}
        writer.writerow(new_row)
