
import csv

with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Extract columns with at least one '1'
keepcols = [c for c in allrows[0] if any(r[c] == '1' for r in allrows)]

# Print the columns to keep for verification
print(keepcols)

# Write to the output CSV
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=keepcols)
    writer.writeheader()  # Write the header
    for row in allrows:
        filtered_row = {c: row[c] for c in keepcols}  # Create a new row with only the kept columns
        writer.writerow(filtered_row)
