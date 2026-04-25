
import csv

# Read the CSV file
reader = csv.DictReader(open("test1.csv", "r"))
allrows = list(reader)

# Get the columns that contain only '1's
keepcols = [c for c in allrows[0] if all(r[c] == '1' for r in allrows)]

# Print the columns to keep
print("Columns to keep:", keepcols)

# Write to a new CSV file with only the selected columns
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=keepcols, extrasaction='ignore')
    writer.writeheader()  # Write the header first
    for row in allrows:
        # Create a new row with only the required columns
        filtered_row = {c: row[c] for c in keepcols}
        writer.writerow(filtered_row)
