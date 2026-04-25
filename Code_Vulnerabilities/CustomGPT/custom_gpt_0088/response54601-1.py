
def count_lines_after_specific_line(fname, specific_line):
    with open(fname) as f:
        lines = f.readlines()

    # Find the index of the specific line
    try:
        specific_index = lines.index(specific_line + '\n')  # Adding newline to match exactly
        # Count the lines after that index
        return len(lines) - specific_index - 1  # Subtract 1 for the specific line itself
    except ValueError:
        return 0  # Return 0 if the specific line is not found

# Example usage
filename = "test.ghx"
line_to_find = "{A   B}"
lines_count = count_lines_after_specific_line(filename, line_to_find)
print(lines_count)
