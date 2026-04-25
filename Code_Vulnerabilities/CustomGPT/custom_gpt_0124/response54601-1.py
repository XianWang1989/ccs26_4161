
def count_lines_after_marker(fname, marker):
    with open(fname) as f:
        count = 0
        found_marker = False

        for line in f:
            # Check if we've found the marker
            if found_marker:
                count += 1
            elif marker in line:
                found_marker = True

    return count

# Example usage
marker = '{A   B}'
line_count = count_lines_after_marker("test.ghx", marker)
print(f"Number of lines after '{marker}': {line_count}")
