
import csv

# Open the CSV file and read it
with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Extract columns with at least one '1'
keepcols = [c for c in allrows[0] if all(any(r[c] == '1' for r in allrows)] and c != 'Title')]

# Print the kept column names for debugging
print(keepcols)

# Prepare the output and write the filtered data to a new CSV file
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=['Title'] + keepcols, extrasaction='ignore')
    writer.writeheader()  # Write the header to the output file
    for row in allrows:
        new_row = {col: row[col] for col in keepcols if col in row}
        new_row['Title'] = row['Title']  # Keep the 'Title' column
        writer.writerow(new_row)
