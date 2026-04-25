
def count_lines_after_keyword(fname, keyword):
    with open(fname) as f:
        lines = f.readlines()  # Read all lines into a list

    # Find the index of the line containing the keyword
    for i, line in enumerate(lines):
        if keyword in line:
            return len(lines) - (i + 1)  # Count lines after the found line

    return 0  # Return 0 if keyword is not found

# Example usage
filename = "test.ghx"
keyword = "{A   B}"
num_lines_after = count_lines_after_keyword(filename, keyword)
print(num_lines_after)
