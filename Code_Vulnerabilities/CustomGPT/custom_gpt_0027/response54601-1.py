
def count_lines_after_specific(fname, specific_line):
    with open(fname) as f:
        lines = f.readlines()

    # Find index of the specific line
    try:
        index = lines.index(specific_line + "\n")
    except ValueError:
        return 0  # Line not found

    # Count lines after the specific line
    return len(lines) - index - 1

# Usage
filename = "test.ghx"
specific_line = "{A   B}"
count = count_lines_after_specific(filename, specific_line)
print(count)
