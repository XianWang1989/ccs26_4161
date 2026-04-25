
import csv

# Read the CSV file and get all rows
with open("test1.csv", "r") as file:
    reader = csv.DictReader(file)
    allrows = list(reader)

# Identify columns to keep based on having values of '1'
keepcols = [c for c in allrows[0] if all(r[c] == '1' for r in allrows)]

# Create a new CSV file to write the filtered columns
with open("output1.csv", "w", newline='') as output_file:
    writer = csv.DictWriter(output_file, fieldnames=['Title'] + keepcols, extrasaction='ignore')
    writer.writeheader()  # Write the header row
    for row in allrows:
        # Create a new row containing only the columns to keep
        filtered_row = {col: row[col] for col in ['Title'] + keepcols}
        writer.writerow(filtered_row)
