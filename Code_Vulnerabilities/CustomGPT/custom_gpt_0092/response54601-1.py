
def count_lines_after_target(file_name, target):
    with open(file_name) as f:
        lines = f.readlines()

    # Find the index of the target line
    try:
        target_index = lines.index(target + '\n')  # Append newline for exact match
        return len(lines) - (target_index + 1)  # Count lines after
    except ValueError:
        return 0  # If target not found

# Example usage
file_name = "test.ghx"
target_line = "{A   B}"

# Call the function and print the result
lines_count = count_lines_after_target(file_name, target_line)
print(lines_count)
