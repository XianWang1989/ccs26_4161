
import csv

# Read the CSV file
reader = csv.DictReader(open("test1.csv", "r"))
allrows = list(reader)

# Keep columns with at least one '1'
keepcols = [c for c in allrows[0] if all(r[c] == '0' for r in allrows) == False]

# Print the columns being kept
print(keepcols)

# Write the filtered columns to the new CSV
with open("output1.csv", "w", newline='') as output_file:
    writer = csv.DictWriter(output_file, fieldnames=keepcols)
    writer.writeheader()  # Write the header
    for row in allrows:
        # Create a new row with only the columns we want to keep
        filtered_row = {key: row[key] for key in keepcols}
        writer.writerow(filtered_row)
