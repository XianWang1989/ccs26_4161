
import csv

# Read data from the input CSV file
with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Identify columns that contain only '1's, except the first column
keepcols = [c for c in allrows[0] if c != 'Title' and any(r[c] == '1' for r in allrows)]

# Print the columns to keep
print(keepcols)

# Write the filtered output to a new CSV file
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=['Title'] + keepcols, extrasaction='ignore')
    writer.writeheader()

    for row in allrows:
        # Create a new dictionary for the row with only the columns we want to keep
        filtered_row = {key: row[key] for key in keepcols if key in row}
        filtered_row['Title'] = row['Title']  # Include the Title column
        writer.writerow(filtered_row)
