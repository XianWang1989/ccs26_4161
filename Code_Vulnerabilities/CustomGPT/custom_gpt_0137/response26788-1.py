
import csv

# Read the CSV file
reader = csv.DictReader(open("test1.csv", "r"))
allrows = list(reader)

# Extract columns where at least one entry has '1'
keepcols = [c for c in allrows[0] if any(r[c] == '1' for r in allrows)]

# Print the columns that will be kept
print(keepcols)

# Create a new CSV with only the relevant columns
with open("output1.csv", "w", newline='') as output_file:
    writer = csv.DictWriter(output_file, fieldnames=keepcols, extrasaction='ignore')
    writer.writeheader()  # Write CSV header
    for row in allrows:
        # Create a new row with only kept columns
        filtered_row = {c: row[c] for c in keepcols}
        writer.writerow(filtered_row)  # Write the filtered row to the output CSV
