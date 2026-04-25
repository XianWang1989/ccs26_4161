
def count_lines_after_marker(fname, marker):
    with open(fname) as f:
        lines = f.readlines()  # Read all lines into a list

    # Initialize a counter and a flag
    count = 0
    found_marker = False

    for line in lines:
        if found_marker:
            count += 1  # Count lines after the marker
        if marker in line:
            found_marker = True  # Marker line found

    return count

# Example usage
marker = "{A   B}"
line_count = count_lines_after_marker("test.ghx", marker)
print(f"Number of lines after '{marker}': {line_count}")
