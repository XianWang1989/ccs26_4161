
with open('reg.fa', 'r') as fh:
    s = ''
    for line in fh:
        # Remove the newline character and append to string
        s += line.strip()  # Use strip() to remove newlines and leading/trailing whitespace

# Print the resulting string
print(s)
