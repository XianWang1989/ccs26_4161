
import csv

# Open the CSV file and read its contents
with open("test1.csv", "r") as file:
    reader = csv.DictReader(file)
    allrows = list(reader)

# Extract columns that have at least one '1'
keepcols = [c for c in allrows[0] if c != 'Title' and any(r[c] == '1' for r in allrows)]

# Print columns to keep
print("Columns to keep:", keepcols)

# Open the output CSV file for writing
with open("output1.csv", "w", newline='') as output_file:
    writer = csv.DictWriter(output_file, fieldnames=['Title'] + keepcols, extrasaction='ignore')
    writer.writeheader()  # Write the header with titles
    for row in allrows:
        # Create a new dictionary for the row that only contains the columns to keep
        new_row = { 'Title': row['Title'] }
        new_row.update({key: row[key] for key in keepcols})
        writer.writerow(new_row)  # Write the filtered row
