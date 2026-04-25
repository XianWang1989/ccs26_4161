
def count_lines_after_specific_line(fname, target_line):
    with open(fname) as f:
        count = 0
        found_target = False

        for line in f:
            if found_target:
                count += 1
            if target_line in line:
                found_target = True

    return count

# Usage
target_line = "{A   B}"
line_count = count_lines_after_specific_line("test.ghx", target_line)
print("Number of lines after '{}': {}".format(target_line, line_count))
