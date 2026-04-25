
def count_lines_after_marker(fname, marker):
    with open(fname, 'r') as f:
        lines = f.readlines()  # Read all lines in the file
        for i, line in enumerate(lines):
            if marker in line:  # Check if the marker line is found
                return len(lines) - (i + 1)  # Count lines after the marker
    return 0  # Return 0 if the marker is not found

# Example usage:
filename = "test.ghx"
marker = "{A   B}"
result = count_lines_after_marker(filename, marker)
print(f"Number of lines after '{marker}': {result}")
