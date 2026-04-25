
# Sample list of companies
companies = ['ABC', 'XYZ', 'XXX', 'DEF', 'XXX', 'GHI']
lineToWrite = ""

# Loop through each company in the list
for newCompany in companies:
    # Check if the current company is 'XXX'
    if newCompany == 'XXX':
        continue  # Skip the rest of the loop for this iteration

    # If the condition is not met, concatenate the company to lineToWrite
    lineToWrite += newCompany + "\t"

# Output the result
print(lineToWrite)  # This will print: ABC     XYZ     DEF     GHI
