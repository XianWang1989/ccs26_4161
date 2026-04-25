
# Sample list of companies
companies = ['ABC', 'XXX', 'DEF', 'GHI']

# Initialize an empty string to collect the lines to write
lineToWrite = ""

# Loop through each company in the list
for company in companies:
    # Check if the current company is 'XXX'
    if company == 'XXX':
        continue  # Skip the rest of the loop body for this iteration

    # If the company is not 'XXX', add it to lineToWrite
    lineToWrite += company + "\t"

# Print the resulting line
print(lineToWrite)
