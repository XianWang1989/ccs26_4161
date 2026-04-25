
import csv

# Read in the CSV file
with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Extract the columns that have at least one '1'
keepcols = [c for c in allrows[0] if all(r[c] != '0' for r in allrows[1:])]

# Print the columns being kept for debugging
print("Columns kept:", keepcols)

# Write to the output CSV file
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=keepcols, extrasaction='ignore')
    writer.writeheader()  # Write the header row
    for row in allrows:
        # Create a new dictionary with only the columns that are kept
        filtered_row = {c: row[c] for c in keepcols}
        writer.writerow(filtered_row)
