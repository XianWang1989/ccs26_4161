
def count_lines_after(fname, target_line):
    count = 0
    found_target = False

    with open(fname, 'r') as f:
        for line in f:
            if found_target:
                count += 1
            if line.strip() == target_line:
                found_target = True

    return count

# Example usage
target = "{A   B}"
line_count = count_lines_after("test.ghx", target)
print(f"Number of lines after '{target}': {line_count}")
