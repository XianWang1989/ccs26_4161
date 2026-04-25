
def count_lines_after_marker(filename, marker):
    with open(filename) as f:
        lines = f.readlines()

    # Find the index of the marker line
    for i, line in enumerate(lines):
        if marker in line:
            # Return count of lines after marker
            return len(lines) - (i + 1)

    # If marker not found, return 0
    return 0

# Usage
filename = "test.ghx"
marker = "{A   B}"
count = count_lines_after_marker(filename, marker)

print(f"Number of lines after '{marker}': {count}")
