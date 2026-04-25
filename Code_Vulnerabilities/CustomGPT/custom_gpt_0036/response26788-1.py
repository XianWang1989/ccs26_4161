
import csv

# Read the CSV file
with open("test1.csv", "r") as file:
    reader = csv.DictReader(file)
    allrows = list(reader)

# Extract columns with only '1's (excluding the first column)
keepcols = [c for c in allrows[0] if c != 'Title' and all(r[c] == '1' for r in allrows)]

# Prepare to write only those columns to a new CSV
with open("output1.csv", "w", newline='') as outfile:
    # Include the first column (names) and the selected columns
    fieldnames = ["Title"] + keepcols
    writer = csv.DictWriter(outfile, fieldnames=fieldnames, extrasaction='ignore')

    # Write header
    writer.writeheader()

    # Write only the desired columns
    for row in allrows:
        # Create a new row with only the selected columns
        new_row = {field: row[field] for field in fieldnames}
        writer.writerow(new_row)

print("Extraction completed. Check output1.csv for results.")
