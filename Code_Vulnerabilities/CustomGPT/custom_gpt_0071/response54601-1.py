
def count_lines_after_specific(fname, specific_line):
    with open(fname) as f:
        lines = f.readlines()

    # Find the index of the specific line
    try:
        index = lines.index(specific_line + "\n")
        # Count the lines after the specific line
        return len(lines) - index - 1
    except ValueError:
        # Return 0 if the specific line is not found
        return 0

# Example usage
filename = "test.ghx"
specific_line = "{A   B}"
line_count = count_lines_after_specific(filename, specific_line)

print(line_count)
