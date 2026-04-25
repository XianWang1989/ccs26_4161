
def count_lines_after_marker(fname, marker):
    with open(fname) as f:
        lines = f.readlines()

    # Find the marker line
    try:
        marker_index = lines.index(marker + "\n")
        # Return the count of lines after the marker
        return len(lines) - (marker_index + 1)
    except ValueError:
        return 0  # Marker not found

# Specify the marker
marker = "{A   B}"
# Count lines after the marker
number_of_lines = count_lines_after_marker("test.ghx", marker)
print(number_of_lines)
