
import csv

# Read the CSV file
with open("test1.csv", "r") as file:
    reader = csv.DictReader(file)
    allrows = list(reader)

# Extract columns that contain at least one '1'
keepcols = [c for c in allrows[0] if c != 'Title' and any(r[c] == '1' for r in allrows)]

# Prepare to write to the output CSV
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=['Title'] + keepcols)
    writer.writeheader()  # Write header
    for row in allrows:
        new_row = {col: row[col] for col in keepcols}
        new_row['Title'] = row['Title']  # Include the 'Title' column
        writer.writerow(new_row)

print("Extraction completed!")
