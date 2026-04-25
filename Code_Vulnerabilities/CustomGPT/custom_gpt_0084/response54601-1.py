
def count_lines_after_specific_line(fname, target):
    with open(fname) as f:
        count = 0
        found_target = False

        for line in f:
            if found_target:
                count += 1
            if target in line:
                found_target = True

    return count

# Example usage
filename = "test.ghx"
target_line = "{A   B}"
lines_after = count_lines_after_specific_line(filename, target_line)
print(f'Number of lines after "{target_line}": {lines_after}')
