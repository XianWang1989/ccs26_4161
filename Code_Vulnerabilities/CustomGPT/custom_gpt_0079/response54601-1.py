
def count_lines_after_marker(fname, marker):
    with open(fname, 'r') as f:
        lines = f.readlines()

    try:
        # Find the index of the line containing the marker
        marker_index = lines.index(marker + '\n')
        # Count the number of lines after the marker
        return len(lines) - (marker_index + 1)
    except ValueError:
        # Marker not found
        return 0

# Specify the marker
marker = "{A   B}"
# Call the function
line_count = count_lines_after_marker("test.ghx", marker)
print(f"Number of lines after '{marker}': {line_count}")
