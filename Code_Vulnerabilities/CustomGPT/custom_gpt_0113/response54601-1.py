
def count_lines_after_target(fname, target):
    with open(fname, 'r') as f:
        lines = f.readlines()

    # Find the index of the target line
    try:
        target_index = lines.index(target + '\n')  # Add newline character
        # Count lines after the target line
        return len(lines) - target_index - 1
    except ValueError:
        # Target line not found
        return 0

# Usage
target_line = "{A   B}"
line_count = count_lines_after_target("test.ghx", target_line)
print(line_count)
