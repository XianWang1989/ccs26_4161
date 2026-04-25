
# Sample list of companies
companies = ['ABC', 'XXX', 'DEF', 'GHI', 'XXX']

# String to hold the result
lineToWrite = ""

# Loop through the companies list
for company in companies:
    # Check if the current company is 'XXX'
    if company == 'XXX':
        continue  # Skip this iteration

    # If it's not 'XXX', append to lineToWrite
    lineToWrite += company + "\t"

# Output the result
print(lineToWrite)
