
def count_lines_after_marker(fname, marker):
    with open(fname, 'r') as f:
        lines = f.readlines()

    # Find the index of the marker
    try:
        index = lines.index(marker + '\n')
        # Count lines after the marker
        return len(lines) - index - 1
    except ValueError:
        return 0  # Marker not found

# Usage
file_name = "test.ghx"
marker = "{A   B}"
number_of_lines = count_lines_after_marker(file_name, marker)
print("Number of lines after {}: {}".format(marker, number_of_lines))
