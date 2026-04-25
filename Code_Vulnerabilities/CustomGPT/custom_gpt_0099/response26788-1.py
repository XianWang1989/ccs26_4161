
import csv

# Read the CSV file
with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Extract columns that only contain '1's
keepcols = [c for c in allrows[0] if all(r[c] != '0' for r in allrows)]

# Write the output to a new CSV file
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=keepcols, extrasaction='ignore')
    writer.writeheader()  # Write the header
    for row in allrows:
        # Create a new dict containing only the columns we want
        new_row = {c: row[c] for c in keepcols}
        writer.writerow(new_row)

print("Filtered columns written to output1.csv")
