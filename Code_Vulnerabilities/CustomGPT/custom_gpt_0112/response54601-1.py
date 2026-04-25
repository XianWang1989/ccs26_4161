
def count_lines_after_marker(fname, marker):
    with open(fname) as f:
        count = 0
        found_marker = False

        for line in f:
            if found_marker:
                count += 1
            elif marker in line:
                found_marker = True

    return count

# Example usage
marker = "{A   B}"
line_count = count_lines_after_marker("test.ghx", marker)
print("Number of lines after '{}': {}".format(marker, line_count))
