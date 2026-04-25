
import csv

# Open the input file and read the rows
with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Extract column headers where all values are not '0'
keepcols = [c for c in allrows[0] if any(r[c] == '1' for r in allrows)]

# Prepare to write to output file with only the needed columns
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=["Title"] + keepcols, extrasaction='ignore')
    writer.writeheader()  # Write the header
    for row in allrows:
        # Create a row only with the selected columns
        new_row = {c: row[c] for c in keepcols}
        new_row["Title"] = row["Title"]  # Include the first column
        writer.writerow(new_row)  # Write the row to the output file
