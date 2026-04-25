
def count_lines_after_marker(fname, marker):
    with open(fname) as f:
        lines = f.readlines()

    # Find the index of the marker
    try:
        marker_index = lines.index(marker + '\n')
        # Count lines after the marker
        count = len(lines) - marker_index - 1
    except ValueError:
        count = 0  # Marker not found

    return count

# Test the function with the specified file
file_name = "test.ghx"
marker = "{A   B}"
result = count_lines_after_marker(file_name, marker)
print(result)
