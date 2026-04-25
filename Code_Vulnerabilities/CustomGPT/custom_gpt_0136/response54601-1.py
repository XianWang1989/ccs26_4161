
def count_lines_after_specific_line(fname, target_line):
    with open(fname) as f:
        count = 0
        found_target = False

        for line in f:
            if found_target:
                count += 1
            elif line.strip() == target_line:
                found_target = True

    return count

# Usage
target = "{A   B}"
line_count = count_lines_after_specific_line("test.ghx", target)
print(f"Number of lines after '{target}': {line_count}")
