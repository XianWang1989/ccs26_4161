
import csv

# Read the CSV file
with open("test1.csv", "r") as f:
    reader = csv.DictReader(f)
    allrows = list(reader)

# Extract column names where all values are not '0'
keepcols = [c for c in allrows[0] if all(r[c] != '0' for r in allrows)]

# Print the columns to keep
print(keepcols)

# Write the filtered rows to new CSV
with open("output1.csv", "w", newline='') as f:
    writer = csv.DictWriter(f, fieldnames=keepcols, extrasaction='ignore')
    writer.writeheader()  # Write the header row
    for row in allrows:
        # Create a new dictionary with only the columns to keep
        filtered_row = {k: row[k] for k in keepcols}
        writer.writerow(filtered_row)
