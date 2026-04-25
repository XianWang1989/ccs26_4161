
def count_lines_after_specific_line(fname, search_string):
    with open(fname, 'r') as f:
        found = False
        line_count = 0

        for line in f:
            if found:
                line_count += 1
            elif search_string in line:
                found = True

    return line_count

# Usage
filename = "test.ghx"
search_string = "{A   B}"
count = count_lines_after_specific_line(filename, search_string)
print(f"Number of lines after '{search_string}': {count}")
