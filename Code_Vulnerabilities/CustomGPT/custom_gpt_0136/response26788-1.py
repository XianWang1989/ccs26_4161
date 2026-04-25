
import csv

# Read the CSV file
with open("test1.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    allrows = list(reader)

# Determine the columns to keep
keepcols = [c for c in allrows[0] if all(r[c] == '1' for r in allrows)]

# Write to the output CSV file
with open("output1.csv", "w", newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=keepcols, extrasaction='ignore')
    writer.writeheader()  # Write the header
    for row in allrows:
        # Create a new row with only the columns to keep
        filtered_row = {c: row[c] for c in keepcols}
        writer.writerow(filtered_row)
