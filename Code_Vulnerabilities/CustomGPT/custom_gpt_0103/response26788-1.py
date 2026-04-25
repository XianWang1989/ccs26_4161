
import csv

# Read from the CSV file
with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Extract columns that contain only 1's (excluding the first column)
keepcols = [c for c in allrows[0] if all(r[c] == '1' for r in allrows)]

# Print the columns we want to keep
print(keepcols)

# Write to a new CSV file
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=['Title'] + keepcols, extrasaction='ignore')
    writer.writeheader()  # Write the header first
    for row in allrows:
        # Create a new row with only the columns we want to keep
        new_row = {key: row[key] for key in ['Title'] + keepcols}
        writer.writerow(new_row)
