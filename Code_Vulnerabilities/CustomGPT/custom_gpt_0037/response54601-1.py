
def count_lines_after(fname, target):
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
line_count = count_lines_after("test.ghx", "{A   B}")
print(line_count)
