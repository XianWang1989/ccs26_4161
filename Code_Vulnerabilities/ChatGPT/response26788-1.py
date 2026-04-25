
import csv

# Read the CSV file into a list of dictionaries
with open("test1.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    allrows = list(reader)

# Identify the columns to keep, which contain at least one '1'
keepcols = [c for c in allrows[0].keys() if c != 'Title' and any(r[c] == '1' for r in allrows)]

# Print the columns that you want to keep for debugging
print("Columns to keep:", keepcols)

# Prepare the output file with only the relevant columns
with open("output1.csv", "w", newline='') as outputfile:
    writer = csv.DictWriter(outputfile, fieldnames=['Title'] + keepcols, extrasaction='ignore')

    # Write the header
    writer.writeheader()

    # Write the rows, ensuring to only include the kept columns
    for row in allrows:
        filtered_row = {col: row[col] for col in keepcols if col in row}
        filtered_row['Title'] = row['Title']  # Preserve the 'Title' column
        writer.writerow(filtered_row)
