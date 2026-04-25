
import csv

# Read the CSV file
with open("test1.csv", "r") as file:
    reader = csv.DictReader(file)
    allrows = list(reader)

# Determine columns to keep (those with '1's)
keepcols = [c for c in allrows[0] if c != 'Title' and all(r[c] == '1' for r in allrows)]

# Prepare to write the output CSV file
with open("output1.csv", "w", newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['Title'] + keepcols, extrasaction='ignore')
    writer.writeheader()  # Write the header
    for row in allrows:
        # Create a new row to write only the 'Title' and the columns to keep
        new_row = {
            'Title': row['Title'],
        }
        new_row.update({col: row[col] for col in keepcols})
        writer.writerow(new_row)
