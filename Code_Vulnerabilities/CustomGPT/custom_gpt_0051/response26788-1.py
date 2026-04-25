
import csv

# Read the CSV file
with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Keep columns that contain at least one '1' (except the first column)
keepcols = [c for c in allrows[0] if c != 'Title' and any(r[c] == '1' for r in allrows)]

# Create a new list of dictionaries with the desired columns
filtered_rows = [{col: row[col] for col in keepcols if col in row} for row in allrows]

# Write the filtered columns to a new CSV file
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=['Title'] + keepcols, extrasaction='ignore')
    writer.writeheader()  # Write the header row
    writer.writerows(filtered_rows)

print("Filtered columns written to output1.csv")
