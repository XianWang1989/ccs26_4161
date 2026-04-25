
import csv

# Open the CSV file and read data
with open("test1.csv", "r") as infile:
    reader = csv.DictReader(infile)
    allrows = list(reader)

# Extract the column names to keep based on the presence of '1'
keepcols = ['Title']  # Start with the first column always
for col in allrows[0].keys():
    if col != 'Title' and any(row[col] == '1' for row in allrows):
        keepcols.append(col)

# Debug print to see which columns will be kept
print("Columns to keep:", keepcols)

# Write to the output CSV file
with open("output1.csv", "w", newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=keepcols, extrasaction='ignore')
    writer.writeheader()  # Write the column headers
    for row in allrows:
        # Filter the row to only include the columns we want to keep
        filtered_row = {key: row[key] for key in keepcols}
        writer.writerow(filtered_row)
