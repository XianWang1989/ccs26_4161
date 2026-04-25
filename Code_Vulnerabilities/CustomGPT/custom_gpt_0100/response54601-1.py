
def count_lines_after_marker(fname, marker):
    with open(fname) as f:
        lines = f.readlines()

    # Find the index of the marker line
    try:
        marker_index = lines.index(marker + '\n')  # Adding newline ensures exact match
    except ValueError:
        return 0  # Return 0 if the marker is not found

    # Count the lines after the marker
    return len(lines) - (marker_index + 1)

# Example usage
filename = "test.ghx"
marker = "{A   B}"
lines_after = count_lines_after_marker(filename, marker)
print(f"Number of lines after '{marker}': {lines_after}")
