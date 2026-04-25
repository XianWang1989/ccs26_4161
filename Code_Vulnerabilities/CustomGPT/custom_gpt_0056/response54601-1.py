
def count_lines_after(fname, target_line):
    with open(fname) as f:
        lines = f.readlines()

    # Find the index of the target line
    try:
        target_index = lines.index(target_line + "\n")  # Adjust for newline character
        count = len(lines) - (target_index + 1)  # Count lines after the target
    except ValueError:
        count = 0  # Target line not found

    return count

# Usage
target_line = "{A   B}"
line_count = count_lines_after("test.ghx", target_line)
print(f"Number of lines after '{target_line}': {line_count}")
