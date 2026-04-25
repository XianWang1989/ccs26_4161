
import csv

# Read the CSV file
with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Determine which columns to keep
keepcols = [c for c in allrows[0] if all(r[c] != '0' for r in allrows)]

# Print the columns that will be kept (for debugging)
print("Columns to keep:", keepcols)

# Write the output to a new CSV file
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=keepcols, extrasaction='ignore')
    writer.writeheader()  # Write the header
    for row in allrows:
        # Keep only the columns specified in keepcols
        new_row = {key: row[key] for key in keepcols}
        writer.writerow(new_row)
