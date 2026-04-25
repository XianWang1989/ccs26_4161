
# Open the file using 'with' to ensure it closes automatically
with open('reg.fa', 'r') as fh:
    # Initialize an empty string to hold your results
    s = ''

    # Iterate through each line in the file
    for line in fh:
        # Remove the newline character and any additional processing
        line = line.strip()  # Removes leading/trailing whitespaces including newline

        # You can process your line here if needed
        # For example, concatenating it to the string `s`
        s += line  # Concatenate the cleaned line to `s`

# After processing all lines, you can print the result
print(s)
