
import csv

# Read the CSV file
with open("test1.csv", "r") as input_file:
    reader = csv.DictReader(input_file)
    allrows = list(reader)

# Keep columns that have at least one '1' in them
keepcols = [c for c in allrows[0] if any(r[c] == '1' for r in allrows)]

print(keepcols)

# Write the filtered columns to the output file
with open("output1.csv", "w", newline='') as output_file:
    writer = csv.DictWriter(output_file, fieldnames=keepcols, extrasaction='ignore')
    writer.writeheader()  # Write the header
    for row in allrows:
        # Create a new row with only the columns we want to keep
        new_row = {col: row[col] for col in keepcols}
        writer.writerow(new_row)
