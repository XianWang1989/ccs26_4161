
import csv

# Read the CSV file and store all rows
with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Determine which columns to keep (those that contain at least one '1')
keepcols = ['Title']  # Start with the title column
for c in allrows[0]:  # Iterate over the columns
    if c == "Title":  # Skip the title column
        continue
    if any(r[c] == '1' for r in allrows):  # Check if column has at least one '1'
        keepcols.append(c)  # Add to keepcols if the condition is met

print("Columns to keep:", keepcols)  # This will show which columns are being kept

# Write the output CSV file
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=keepcols, extrasaction='ignore')
    writer.writeheader()  # Write header first
    writer.writerows([{c: r[c] for c in keepcols} for r in allrows])  # Only keep relevant columns

print("Output written to output1.csv.")
