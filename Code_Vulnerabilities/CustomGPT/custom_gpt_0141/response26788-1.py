
import csv

# Read the original CSV file
with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Determine which columns to keep (those with at least one '1')
keepcols = [c for c in allrows[0] if c != 'Title' and any(r[c] == '1' for r in allrows)]

print("Columns to keep:", keepcols)

# Write the filtered columns to a new CSV file
if keepcols:  # Check if there are any columns to write
    with open("output1.csv", "w", newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=keepcols, extrasaction='ignore')
        writer.writeheader()  # Write header row
        for row in allrows:
            # Create a new dict for only the columns we want to keep
            filtered_row = {c: row[c] for c in keepcols} 
            writer.writerow(filtered_row)
else:
    print("No columns with '1's found.")
