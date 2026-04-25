
import csv

# Read the CSV file
with open("test1.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    allrows = list(reader)

# Identify columns to keep (excluding the first column)
keepcols = [c for c in allrows[0] if c != 'Title' and any(r[c] == '1' for r in allrows)]

# Write the result to a new CSV file
with open("output1.csv", "w", newline='') as outputfile:
    writer = csv.DictWriter(outputfile, fieldnames=['Title'] + keepcols, extrasaction='ignore')
    writer.writeheader()  # Write the header
    for row in allrows:
        # Keep only the relevant columns
        output_row = {col: row[col] for col in keepcols if col in row}
        output_row['Title'] = row['Title']  # Include the title column
        writer.writerow(output_row)
