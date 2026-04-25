
def count_lines_after_target(fname, target):
    count = 0
    found_target = False

    with open(fname) as f:
        for line in f:
            if found_target:
                # We only count lines after the target line has been found
                count += 1
            elif target in line:
                # If we find the target line, set the flag to True
                found_target = True

    return count

# Example usage
filename = "test.ghx"
target_line = "{A   B}"
count = count_lines_after_target(filename, target_line)
print(f"Number of lines after '{target_line}': {count}")
