
def count_lines_after_specific_line(fname, target_line):
    count = 0
    found_target = False

    with open(fname) as f:
        for line in f:
            # Check if the target line is found
            if found_target:
                count += 1  # Increment the count after the target line
            if target_line in line:
                found_target = True  # Set the flag to True if the target line is found

    return count

# Example usage
filename = "test.ghx"
target = "{A   B}"
lines_after_count = count_lines_after_specific_line(filename, target)
print(f"Number of lines after '{target}': {lines_after_count}")
