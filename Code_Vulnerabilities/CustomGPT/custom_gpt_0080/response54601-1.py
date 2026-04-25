
def count_lines_after(filename, target):
    after_target = False
    line_count = 0

    with open(filename) as f:
        for line in f:
            if after_target:
                line_count += 1
            if target in line:
                after_target = True

    return line_count

# Example usage
target_line = "{A   B}"
line_count = count_lines_after("test.ghx", target_line)
print(line_count)
