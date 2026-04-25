
def count_lines_after_specific_line(fname, target):
    with open(fname) as f:
        lines = f.readlines()

    # Find the index of the target line
    try:
        target_index = lines.index(target + '\n')
        # Count lines after the target line
        return len(lines) - (target_index + 1)
    except ValueError:
        return 0  # Target line not found

# Example usage
filename = "test.ghx"
target_line = "{A   B}"
count = count_lines_after_specific_line(filename, target_line)
print(count)
