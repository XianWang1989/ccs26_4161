
def count_lines_after_target(fname, target_line):
    with open(fname) as f:
        lines = f.readlines()

    # Find index of the target line
    if target_line in lines:
        index = lines.index(target_line)
        # Count lines after the target line
        return len(lines) - index - 1
    else:
        return 0  # Target line not found

# Example usage
filename = "test.ghx"
target = "{A   B}\n"  # Ensure to include the newline character
line_count = count_lines_after_target(filename, target)
print(line_count)
