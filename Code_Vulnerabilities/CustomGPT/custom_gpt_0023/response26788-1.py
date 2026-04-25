
import csv

# Read the CSV file
with open("test1.csv", "r") as file:
    reader = csv.DictReader(file)
    allrows = list(reader)

# Identify columns to keep
keepcols = [c for c in allrows[0] if any(r[c] == '1' for r in allrows)]

# Print the columns to keep for debugging
print("Columns to keep:", keepcols)

# Write the filtered rows to a new CSV file
with open("output1.csv", "w", newline='') as output_file:
    writer = csv.DictWriter(output_file, fieldnames=keepcols, extrasaction='ignore')
    writer.writeheader()  # Write header row
    for row in allrows:
        # Create a new row containing only the columns to keep
        filtered_row = {c: row[c] for c in keepcols}
        writer.writerow(filtered_row)
