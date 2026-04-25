
def count_lines_after_specific_line(fname, target):
    with open(fname) as f:
        lines = f.readlines()

    # Find the index of the target line
    try:
        index = lines.index(target + '\n')  # Include newline character
        return len(lines) - index - 1  # Count lines after the target
    except ValueError:
        return 0  # Target line not found

# Example usage
t = count_lines_after_specific_line("test.ghx", "{A   B}")
print(t)
