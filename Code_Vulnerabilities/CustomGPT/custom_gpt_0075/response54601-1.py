
def count_lines_after_marker(filename, marker):
    with open(filename, 'r') as f:
        lines = f.readlines()

    # Find the marker line
    if marker in lines:
        # Return count of lines after the marker
        return len(lines[lines.index(marker) + 1:])
    else:
        return 0  # Marker not found

# Example usage
count = count_lines_after_marker("test.ghx", "{A   B}")
print(count)
