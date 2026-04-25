
def count_lines_after_marker(filename, marker):
    with open(filename, 'r') as f:
        lines = f.readlines()  # Read all lines into a list

    # Find the index of the line that contains the marker
    try:
        marker_index = lines.index(marker + '\n')  # Adding newline for exact match
    except ValueError:
        print("Marker not found.")
        return 0

    # Return the number of lines after the marker
    return len(lines) - marker_index - 1

# Example usage
filename = "test.ghx"
marker = "{A   B}"
lines_after_marker = count_lines_after_marker(filename, marker)
print(f"Number of lines after '{marker}': {lines_after_marker}")
