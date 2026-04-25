
def count_lines_after_target(fname, target):
    with open(fname) as f:
        found = False
        count = 0

        for line in f:
            if found:
                count += 1  # Count lines after the target line
            elif target in line:
                found = True  # Set flag to start counting after target

    return count

# Example usage:
file_path = "test.ghx"
target_line = "{A   B}"
line_count = count_lines_after_target(file_path, target_line)
print(line_count)
