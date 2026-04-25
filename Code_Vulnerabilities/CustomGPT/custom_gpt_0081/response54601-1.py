
def count_lines_after_specific_line(fname, specific_line):
    with open(fname) as f:
        found = False
        count = 0
        for line in f:
            # Check if the current line matches the specific line
            if found:
                count += 1  # Increment count after finding the specific line
            if line.strip() == specific_line:  # Use strip to ignore leading/trailing whitespace
                found = True  # Set flag to indicate that we've found the specific line

    return count

# Define the specific line you are looking for
specific_line = "{A   B}"

# Call the function and print the result
line_count = count_lines_after_specific_line("test.ghx", specific_line)
print(f"Number of lines after '{specific_line}': {line_count}")
