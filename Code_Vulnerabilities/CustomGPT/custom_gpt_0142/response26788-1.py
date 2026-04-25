
import csv

# Read the input CSV file
with open("test1.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    allrows = list(reader)  # Convert reader to a list of dictionaries

# Determine which columns to keep (excluding the first column)
keepcols = [c for c in allrows[0] if c != 'Title' and all(r[c] == '1' for r in allrows)]

# Output the columns to be kept for debugging
print("Columns to keep:", keepcols)

# Write to a new CSV file
with open("output1.csv", "w", newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['Title'] + keepcols, extrasaction='ignore')

    writer.writeheader()  # Write the header to the output file
    for row in allrows:
        new_row = {key: row[key] for key in ['Title'] + keepcols}  # Create a new row only with the kept columns
        writer.writerow(new_row)  # Write the new row to the output CSV
