
def count_lines_after_specific_line(fname, target_line):
    with open(fname) as f:
        lines = f.readlines()

    target_index = None

    # Find the index of the target line
    for index, line in enumerate(lines):
        if target_line in line:
            target_index = index
            break

    # If the target line was found, count the lines after it
    if target_index is not None:
        count = len(lines) - target_index - 1
        return count
    else:
        return 0  # Target line not found

# Example usage
filename = "test.ghx"
target = "{A   B}"
line_count = count_lines_after_specific_line(filename, target)
print("Number of lines after '{}': {}".format(target, line_count))
