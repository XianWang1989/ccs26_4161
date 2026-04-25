
import csv

# Open and read the CSV file
with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Identify columns with at least one '1'
keepcols = [c for c in allrows[0] if all(r[c] == '1' for r in allrows)]

# Check if keepcols is not empty
if keepcols:
    print(keepcols)

    # Write the extracted columns to a new CSV file
    with open("output1.csv", "w", newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=keepcols, extrasaction='ignore')
        writer.writeheader()  # Write the header
        for row in allrows:
            # Create a new row with only the cols we want to keep
            new_row = {key: row[key] for key in keepcols}
            writer.writerow(new_row)
else:
    print("No columns with '1' found.")
