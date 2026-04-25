
def count_lines_after_marker(fname, marker):
    with open(fname) as f:
        lines = f.readlines()

    # Initialize a flag and a counter
    found_marker = False
    count = 0

    for line in lines:
        # Check if the current line contains the marker
        if marker in line:
            found_marker = True
            continue  # Skip the marker line itself

        # If the marker has been found, count subsequent lines
        if found_marker:
            count += 1

    return count

# Example usage
marker = "{A   B}"
line_count = count_lines_after_marker("test.ghx", marker)
print("Number of lines after the marker:", line_count)
