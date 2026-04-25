
def count_lines_after_specific_line(fname, target_line):
    with open(fname) as f:
        # Initialize a flag to indicate if we've found the target line
        found_target = False
        # Initialize a counter for lines after the target line
        line_count = 0

        for line in f:
            # Check if the current line is the target line
            if found_target:
                line_count += 1
            elif line.strip() == target_line:
                found_target = True

    return line_count

# Example usage
target = "{A   B}"
line_count = count_lines_after_specific_line("test.ghx", target)
print(f"Number of lines after '{target}': {line_count}")
