
def count_lines_after_specific_line(fname, target):
    with open(fname) as f:
        lines = f.readlines()

    # Find the index of the target line
    try:
        target_index = lines.index(target) + 1  # To get the line after the target
    except ValueError:
        return 0  # Return 0 if the target line is not found

    # Count the lines after the target line
    return len(lines) - target_index

# Example usage
filename = "test.ghx"
target_line = "{A   B}\n"  # Ensure to match newline character
line_count = count_lines_after_specific_line(filename, target_line)
print(f"Number of lines after '{target_line.strip()}': {line_count}")
