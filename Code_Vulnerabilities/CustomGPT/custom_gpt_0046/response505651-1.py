
# Sample list of companies
companies = ['ABC', 'XXX', 'DEF', 'XYZ']

# Variable to store lines to write
lineToWrite = ""

# Loop through the list of companies
for company in companies:
    if company == 'XXX':
        continue  # Skip this iteration if company is 'XXX'

    lineToWrite += company + "\t"  # Add the company to the lineToWrite

print(lineToWrite.strip())  # Output the result
