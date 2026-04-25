
import csv

# Read the CSV file
with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Keep columns that have at least one '1'
keepcols = [c for c in allrows[0] if all(r[c] != '0' for r in allrows)]

# Print the columns to be kept
print(keepcols)

# Write the filtered columns to a new CSV file
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=keepcols, extrasaction='ignore')
    writer.writeheader()  # Write column titles
    for row in allrows:
        # Create a new dictionary with only the desired columns
        filtered_row = {c: row[c] for c in keepcols}
        writer.writerow(filtered_row)
