
def count_lines_after_marker(fname, marker):
    with open(fname) as f:
        lines = f.readlines()

    # Find the index of the marker
    try:
        index = lines.index(marker + '\n')  # Include newline character
        return len(lines) - index - 1  # Count lines after the marker
    except ValueError:
        return 0  # Marker not found

# Example usage
file_name = "test.ghx"
marker = "{A   B}"
count = count_lines_after_marker(file_name, marker)
print(f"Number of lines after '{marker}': {count}")
