
import csv

# Reading the CSV file
with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Keeping columns that contain only '1's (except the first column)
keepcols = [c for c in allrows[0] if c != 'Title' and all(r[c] == '1' for r in allrows)]

# Writing to the output file
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=['Title'] + keepcols, extrasaction='ignore')
    writer.writeheader()  # Write the header first
    for row in allrows:
        # Filter the row to keep only the 'Title' and the selected columns
        filtered_row = {key: row[key] for key in ['Title'] + keepcols}
        writer.writerow(filtered_row)

print("Columns extracted and written to output1.csv:", keepcols)
