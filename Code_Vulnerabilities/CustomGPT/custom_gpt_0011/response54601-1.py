
def count_lines_after_specific_line(fname, specific_line):
    with open(fname) as f:
        lines = f.readlines()  # Read all lines in the file
        # Find the index of the specific line
        try:
            index = lines.index(specific_line)  # Get the index of the specific line
            return len(lines) - index - 1  # Count lines after the specific line
        except ValueError:
            return 0  # Return 0 if the specific line is not found

specific_line = "{A   B}\n"  # Note the newline character at the end
count = count_lines_after_specific_line("test.ghx", specific_line)
print(count)
