
import csv

# Read the CSV file
with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Identify columns to keep based on the presence of '1's
keepcols = [c for c in allrows[0] if all(r[c] == '1' for r in allrows)]

# Print out the columns to keep for verification
print("Columns to keep:", keepcols)

# Write the filtered columns to a new CSV file
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=keepcols)
    writer.writeheader()  # Write the header
    for row in allrows:
        filtered_row = {c: row[c] for c in keepcols}  # Create a new row with only the columns to keep
        writer.writerow(filtered_row)
