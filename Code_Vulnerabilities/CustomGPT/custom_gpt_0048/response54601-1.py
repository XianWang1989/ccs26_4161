
def count_lines_after_target(fname, target_line):
    with open(fname) as f:
        found_target = False
        count = 0

        for line in f:
            if found_target:
                count += 1
            if line.strip() == target_line:
                found_target = True

    return count

# Example usage
target = "{A   B}"
line_count = count_lines_after_target("test.ghx", target)
print("Number of lines after '{}': {}".format(target, line_count))
