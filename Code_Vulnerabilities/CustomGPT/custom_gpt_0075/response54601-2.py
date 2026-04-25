
def count_lines_after_marker(filename, marker):
    count = 0
    marker_found = False

    with open(filename, 'r') as f:
        for line in f:
            if marker_found:
                count += 1
            if line.strip() == marker:
                marker_found = True  # Start counting after finding the marker

    return count

# Example usage
count = count_lines_after_marker("test.ghx", "{A   B}")
print(count)
