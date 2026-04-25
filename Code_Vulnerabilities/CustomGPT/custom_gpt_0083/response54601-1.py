
def count_lines_after(filename, target_line):
    with open(filename) as f:
        lines = f.readlines()

    # Find the index of the target line
    try:
        index = lines.index(target_line + '\n')  # Include newline character
        return len(lines) - index - 1  # Subtract 1 for the target line itself
    except ValueError:
        return 0  # Return 0 if the target line is not found

# Usage example
filename = "test.ghx"
target_line = "{A   B}"
line_count = count_lines_after(filename, target_line)
print(line_count)
