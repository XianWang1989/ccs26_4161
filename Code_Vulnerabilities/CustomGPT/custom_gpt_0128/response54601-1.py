
def count_lines_after(filename, target_line):
    with open(filename) as f:
        lines = f.readlines()  # Read all lines into a list

    # Find the index of the target line
    try:
        index = lines.index(target_line)
        # Count the number of lines after the target line
        return len(lines) - index - 1
    except ValueError:
        # Target line not found
        return 0

# Use the function
filename = "test.ghx"
target_line = "{A   B}\n"  # Ensure there's a newline at the end
line_count = count_lines_after(filename, target_line)
print(line_count)
