
def count_lines_after_marker(filename, marker):
    count = 0
    found_marker = False

    with open(filename) as f:
        for line in f:
            if found_marker:
                count += 1
            if marker in line:
                found_marker = True

    return count

# Example usage
marker = "{A   B}"
line_count = count_lines_after_marker("test.ghx", marker)
print(line_count)
