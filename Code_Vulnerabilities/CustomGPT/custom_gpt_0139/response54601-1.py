
def count_lines_after_marker(fname, marker):
    with open(fname) as f:
        lines = f.readlines()  # Read all lines into a list

    # Find the index of the line that contains the marker
    for index, line in enumerate(lines):
        if marker in line:
            # Return the count of lines after the marker
            return len(lines) - (index + 1)  # Lines after the marker

    # If the marker is not found, return 0
    return 0

# Specifying the filename and marker
filename = "test.ghx"
marker = "{A   B}"

# Counting the lines after the specified marker
line_count = count_lines_after_marker(filename, marker)
print(f"Number of lines after '{marker}': {line_count}")
