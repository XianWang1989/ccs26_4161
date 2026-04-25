
def count_lines_after_specific_line(fname, target_line):
    count = 0
    found_target = False

    with open(fname, 'r') as f:
        for line in f:
            if found_target:
                count += 1
            if target_line in line:
                found_target = True

    return count

# Example usage
file_name = "test.ghx"
target_string = "{A   B}"
lines_count = count_lines_after_specific_line(file_name, target_string)
print(f"Number of lines after '{target_string}': {lines_count}")
