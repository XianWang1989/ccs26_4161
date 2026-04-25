
import csv

# Read the CSV file
with open("test1.csv", "r") as f:
    reader = csv.DictReader(f)
    allrows = list(reader)

# Extract columns with at least one '1'
keepcols = [c for c in allrows[0] if c != 'Title' and any(r[c] == '1' for r in allrows)]

# Write the output CSV file with the selected columns
with open("output1.csv", "w", newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['Title'] + keepcols, extrasaction='ignore')
    writer.writeheader()

    for row in allrows:
        # Create a new row with only the columns to keep
        new_row = {col: row[col] for col in keepcols if col in row}
        new_row['Title'] = row['Title']  # Always keep the Title column
        writer.writerow(new_row)
