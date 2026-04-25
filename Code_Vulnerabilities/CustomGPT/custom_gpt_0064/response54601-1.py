
def count_lines_after_marker(fname, marker):
    with open(fname) as f:
        lines = f.readlines()

    # Find the index of the line containing the marker
    for index, line in enumerate(lines):
        if marker in line:
            # Return the count of lines after the marker
            return len(lines) - index - 1

    return 0  # Return 0 if the marker is not found

# Specify the file name and the marker
file_name = "test.ghx"
marker = "{A   B}"

# Use the function and print the result
line_count = count_lines_after_marker(file_name, marker)
print(line_count)
