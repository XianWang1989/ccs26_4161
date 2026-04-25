
import csv

# Read the CSV file
with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Keep columns that contain 1's, excluding the first column (the title)
keepcols = [c for c in allrows[0] if c != 'Title' and any(r[c] == '1' for r in allrows)]

# Print the columns to be kept
print(keepcols)

# Write the filtered rows to a new CSV file
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=['Title'] + keepcols, extrasaction='ignore')
    writer.writeheader()
    for row in allrows:
        if any(row[c] == '1' for c in keepcols):
            writer.writerow(row)
