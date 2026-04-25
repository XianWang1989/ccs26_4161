
def count_lines_after_marker(filename, marker):
    with open(filename, 'r') as f:
        lines = f.readlines()

    # Find the position of the marker
    marker_found = False
    count = 0

    for line in lines:
        if marker_found:
            count += 1
        if marker in line:
            marker_found = True

    return count

# Usage
filename = "test.ghx"
marker = "{A   B}"
lines_count = count_lines_after_marker(filename, marker)
print(f"Number of lines after '{marker}': {lines_count}")
