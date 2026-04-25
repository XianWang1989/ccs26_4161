
import csv

# Open the CSV file for reading
with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Determine the columns to keep (those that contain '1's)
keepcols = [c for c in allrows[0] if all(r[c] == '1' for r in allrows)]

# Create a new CSV file for writing
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=['Title'] + keepcols, extrasaction='ignore')
    writer.writeheader()

    # Write only the rows with the keepcols
    for row in allrows:
        # Create a new row containing only the 'Title' and the kept columns
        new_row = {key: row[key] for key in ['Title'] + keepcols}
        writer.writerow(new_row)

print("Extraction complete. Please check 'output1.csv'.")
