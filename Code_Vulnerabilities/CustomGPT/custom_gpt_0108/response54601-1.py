
def count_lines_after_target(fname, target):
    with open(fname) as f:
        lines = f.readlines()  # Read all lines into a list

    # Find the index of the target line
    try:
        target_index = lines.index(target)  # Get the index of the target line
        return len(lines) - (target_index + 1)  # Count lines after the target line
    except ValueError:
        return 0  # Target line not found

# Example use
filename = "test.ghx"
target_line = "{A   B}\n"  # Note the newline character

line_count = count_lines_after_target(filename, target_line)
print(f"Number of lines after '{target_line.strip()}': {line_count}")
