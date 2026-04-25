
def count_lines_after(filename, search_line):
    with open(filename) as f:
        lines = f.readlines()

    # Find the index of the search line
    try:
        index = lines.index(search_line + '\n')  # + '\n' to match the line format
    except ValueError:
        return 0  # Return 0 if the line is not found

    # Count the lines after the index
    return len(lines) - index - 1

# Example usage
filename = "test.ghx"
search_line = "{A   B}"
count = count_lines_after(filename, search_line)
print(count)
