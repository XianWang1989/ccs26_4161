
import csv

# Read the CSV file
with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Identify the columns that have at least one '1'
keepcols = [c for c in allrows[0] if c != 'Title' and any(r[c] == '1' for r in allrows)]

# Print the columns that will be kept
print("Columns to keep:", keepcols)

# Write the filtered rows to the output CSV file
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=['Title'] + keepcols, extrasaction='ignore')
    writer.writeheader()  # Writes the header including 'Title'

    # Write only the columns we want
    for row in allrows:
        filtered_row = {'Title': row['Title']}
        for col in keepcols:
            filtered_row[col] = row[col]
        writer.writerow(filtered_row)
