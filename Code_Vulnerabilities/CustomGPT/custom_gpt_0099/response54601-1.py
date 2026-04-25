
def count_lines_after_marker(fname, marker):
    with open(fname) as f:
        count = 0
        found_marker = False

        for line in f:
            if found_marker:
                count += 1  # Count lines after the marker
            elif marker in line:
                found_marker = True  # Marker found, start counting lines

    return count

# Example usage
marker = "{A   B}"
num_lines_after = count_lines_after_marker("test.ghx", marker)
print(num_lines_after)
