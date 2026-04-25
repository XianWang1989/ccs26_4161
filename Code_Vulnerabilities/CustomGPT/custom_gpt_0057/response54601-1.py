
def count_lines_after_marker(filename, marker):
    with open(filename, 'r') as file:
        lines = file.readlines()
        marker_index = next((i for i, line in enumerate(lines) if marker in line), None)
        if marker_index is not None:
            return len(lines) - marker_index - 1
        return 0

filename = "test.ghx"
marker = "{A   B}"
count = count_lines_after_marker(filename, marker)
print(f"Number of lines after '{marker}': {count}")
