
def count_lines_after_specific_line(fname, target_line):
    with open(fname) as f:
        lines = f.readlines()  # Read all lines into a list
        for i, line in enumerate(lines):
            if target_line in line:
                return len(lines) - (i + 1)  # Count lines after the target line
    return 0  # Return 0 if target line is not found

# Example usage
target = '{A   B}'
line_count = count_lines_after_specific_line("test.ghx", target)
print(f'Number of lines after "{target}": {line_count}')
