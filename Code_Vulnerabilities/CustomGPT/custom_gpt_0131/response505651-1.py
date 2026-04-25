
lineToWrite = ""

for x in line:
    if x == 'XXX':  # Check the current item x, not newCompany
        continue
    else:
        lineToWrite += x + "\t"  # Append the current valid company to the lineToWrite

# Now lineToWrite will contain the list of companies excluding 'XXX'
