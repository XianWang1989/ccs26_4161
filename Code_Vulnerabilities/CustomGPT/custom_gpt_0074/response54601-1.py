
def count_lines_after_specific_line(fname, target_line):
    with open(fname) as f:
        count = 0
        found_target = False  # Flag to indicate if the target line has been found

        for line in f:
            if found_target:
                count += 1  # Increment the count for each line after the target
            # Check if the current line matches the target line
            if target_line in line:
                found_target = True  # Set the flag to True when the target line is found

    return count

# Usage
filename = "test.ghx"
target = "{A   B}"
lines_after_count = count_lines_after_specific_line(filename, target)
print(f'Number of lines after "{target}": {lines_after_count}')
