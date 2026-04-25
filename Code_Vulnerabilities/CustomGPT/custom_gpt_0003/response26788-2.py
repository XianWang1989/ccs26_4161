
import csv

# Read the CSV file
with open("test1.csv", "r") as file:
    reader = csv.DictReader(file)
    allrows = list(reader)

# Extract columns that contain at least one '1' across all rows
keepcols = [c for c in allrows[0].keys() if c != 'Title' and any(r[c] == '1' for r in allrows)]

# Output the results
print("Columns to keep:", keepcols)

# Write the filtered data to output file
with open("output1.csv", "w", newline='') as output_file:
    writer = csv.DictWriter(output_file, fieldnames=['Title'] + keepcols, extrasaction='ignore')
    writer.writeheader()  # Write the header
    for row in allrows:
        # Create a filtered row only with the columns to keep
        filtered_row = {k: row[k] for k in ['Title'] + keepcols}
        writer.writerow(filtered_row)
