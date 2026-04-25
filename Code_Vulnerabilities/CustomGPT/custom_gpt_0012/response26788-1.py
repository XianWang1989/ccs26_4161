
import csv

# Read the CSV file
with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Extract columns with '1's, leaving the first column intact
keepcols = [c for c in allrows[0] if c == 'Title' or any(r[c] == '1' for r in allrows)]

# Write to a new CSV file
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=keepcols)
    writer.writeheader()  # Write the header first
    for row in allrows:
        # Create a new dictionary with only the columns we want
        filtered_row = {c: row[c] for c in keepcols}
        writer.writerow(filtered_row)
