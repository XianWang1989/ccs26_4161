
def count_lines_after_target(fname, target):
    with open(fname) as f:
        lines = f.readlines()

    # Find the index of the line containing the target
    for index, line in enumerate(lines):
        if target in line:
            # Count and return the number of lines after this index
            return len(lines) - (index + 1)

    # Return 0 if the target is not found
    return 0

# Example usage
file_name = "test.ghx"
target_line = "{A   B}"
line_count = count_lines_after_target(file_name, target_line)
print(line_count)
