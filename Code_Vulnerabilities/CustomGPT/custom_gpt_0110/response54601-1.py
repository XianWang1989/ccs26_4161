
def count_lines_after_specific_line(filename, target_line):
    with open(filename, 'r') as f:
        lines = f.readlines()

    # Find the index of the target line
    try:
        target_index = lines.index(target_line + '\n')  # +'\n' to match the newline character
        count_after = len(lines) - target_index - 1  # Count lines after the target line
    except ValueError:
        # If the target line is not found
        count_after = 0

    return count_after

# Example usage
file_name = "test.ghx"
target = "{A   B}"
result = count_lines_after_specific_line(file_name, target)
print(f'Number of lines after "{target}": {result}')
