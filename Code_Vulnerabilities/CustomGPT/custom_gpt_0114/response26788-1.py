
import csv

# Read the CSV file
with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Extract columns that contain only 1's
keepcols = ['Title'] + [c for c in allrows[0] if all(r[c] == '1' for r in allrows)]

# Write the filtered columns to a new CSV
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=keepcols)
    writer.writeheader()  # Write the header
    for row in allrows:
        # Create a dict with only the columns we want to keep
        filtered_row = {c: row[c] for c in keepcols}
        writer.writerow(filtered_row)
