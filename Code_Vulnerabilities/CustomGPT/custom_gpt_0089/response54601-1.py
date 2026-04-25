
def count_lines_after(filename, search_line):
    with open(filename) as f:
        count = 0
        found = False

        for line in f:
            if found:
                count += 1
            elif line.strip() == search_line:
                found = True

    return count

# Usage example
filename = "test.ghx"
search_line = "{A   B}"
line_count = count_lines_after(filename, search_line)
print(f"Number of lines after '{search_line}': {line_count}")
