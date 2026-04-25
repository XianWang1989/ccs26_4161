
def count_lines_after_marker(fname, marker):
    with open(fname) as f:
        lines = f.readlines()  # Read all lines into a list

    # Find the marker and count lines after it
    try:
        marker_index = lines.index(marker)  # Get the index of the marker
        return len(lines) - (marker_index + 1)  # Count lines after the marker
    except ValueError:
        return 0  # Marker not found

# Usage
marker = "{A   B}\n"  # Ensure the marker includes the newline character
count = count_lines_after_marker("test.ghx", marker)
print(f"Number of lines after '{marker.strip()}': {count}")
