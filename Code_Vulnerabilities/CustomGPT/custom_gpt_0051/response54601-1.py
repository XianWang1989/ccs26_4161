
def count_lines_after_marker(filename, marker):
    found_marker = False
    count = 0

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
print(f"Number of lines after '{marker}': {line_count}")
