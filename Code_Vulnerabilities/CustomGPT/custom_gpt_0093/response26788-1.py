
import csv

# Read data from the CSV file
with open("test1.csv", "r") as file:
    reader = csv.DictReader(file)
    allrows = list(reader)

# Identify columns to keep (columns with at least one '1')
keepcols = [c for c in allrows[0] if c != 'Title' and any(r[c] == '1' for r in allrows)]

# Print the columns that will be kept
print(keepcols)

# Write to the output file
with open("output1.csv", "w", newline='') as output_file:
    writer = csv.DictWriter(output_file, fieldnames=['Title'] + keepcols, extrasaction='ignore')
    writer.writeheader()
    for row in allrows:
        # Create a new row only with "keepcols"
        new_row = {col: row[col] for col in keepcols}
        new_row['Title'] = row['Title']  # Add the title column
        writer.writerow(new_row)
