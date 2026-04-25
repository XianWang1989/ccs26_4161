
def count_lines_after_specified_line(filename, specified_line):
    count = 0
    found = False

    with open(filename, 'r') as file:
        for line in file:
            if found:
                count += 1  # Increment count for each line after the specified line
            if specified_line in line:
                found = True  # Set found to True when specified line is found

    return count

# Usage
filename = "test.ghx"  # Replace with your actual file path
specified_line = "{A   B}"  # The line to look for
lines_count = count_lines_after_specified_line(filename, specified_line)

print(f"Number of lines after '{specified_line}': {lines_count}")
