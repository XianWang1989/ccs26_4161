
def count_lines_after(filename, search_line):
    with open(filename, 'r') as file:
        found = False
        line_count = 0

        for line in file:
            if found:  # If we've found the search_line already
                line_count += 1
            if search_line in line:  # Check if the current line contains the search_line
                found = True

    return line_count

# Example usage
filename = "test.ghx"
search_line = "{A   B}"
result = count_lines_after(filename, search_line)
print(f"Number of lines after '{search_line}': {result}")
