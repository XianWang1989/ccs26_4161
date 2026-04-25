
def count_lines_after_specific_line(fname, target):
    with open(fname, 'r') as f:
        lines = f.readlines()

    # Find the target line
    try:
        index = lines.index(target + '\n')  # Adjust for newline
        count = len(lines) - (index + 1)  # Count lines after the target
    except ValueError:
        count = 0  # Target line not found

    return count

# Usage
target_line = "{A   B}"
line_count = count_lines_after_specific_line("test.ghx", target_line)
print(line_count)
