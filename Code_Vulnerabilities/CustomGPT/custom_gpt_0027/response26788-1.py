
import csv

# Read the CSV file
with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Identify columns with at least one '1'
keepcols = [c for c in allrows[0] if all(r[c] != '0' for r in allrows)]

# Print the columns to keep for debugging
print("Columns to keep:", keepcols)

# Write the filtered rows to a new CSV file
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=keepcols, extrasaction='ignore')
    writer.writeheader()  # Write the header
    for row in allrows:
        filtered_row = {k: v for k, v in row.items() if k in keepcols}
        writer.writerow(filtered_row)
