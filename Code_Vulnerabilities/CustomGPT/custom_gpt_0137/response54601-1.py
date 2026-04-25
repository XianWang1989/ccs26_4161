
def count_lines_after_specific_line(fname, specific_line):
    count = 0
    found = False

    with open(fname) as f:
        for line in f:
            if found:  # If we've already found the specific line, count further lines
                count += 1
            if specific_line in line:  # Check if the specific line is found
                found = True

    return count

# Use the function
lines_after = count_lines_after_specific_line("test.ghx", "{A   B}")
print(f"Number of lines after '{'{A   B}'}': {lines_after}")
