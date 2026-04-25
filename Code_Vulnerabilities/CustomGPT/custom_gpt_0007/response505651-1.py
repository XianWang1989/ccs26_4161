
# Example list of companies
companies = ['ABC', 'DEF', 'XXX', 'GHI', 'JKL']

# Initialize an empty string to hold the line to write
lineToWrite = ""

for newCompany in companies:
    if newCompany == 'XXX':  # Check if the company is 'XXX'
        continue  # Skip to the next iteration if the condition is met
    else:
        lineToWrite += newCompany + "\t"  # Append to lineToWrite if the condition is not met

# Output the final result
print(lineToWrite.strip())  # Print the result, stripping any trailing tabs
