
import csv

# Open the CSV file and read its contents
with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Extract columns that do not solely contain '0's
keepcols = [c for c in allrows[0] if c != 'Title' and all(r[c] != '0' for r in allrows)]

# Print the names of columns being kept for verification
print(keepcols)

# Write the output to a new CSV file
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=['Title'] + keepcols)
    writer.writeheader()  # Write the header for the output file
    for row in allrows:
        # Prepare a row to write only the required columns
        filtered_row = {k: row[k] for k in keepcols if k in row}
        # Write the filtered row to the output file
        writer.writerow({'Title': row['Title'], **filtered_row})
