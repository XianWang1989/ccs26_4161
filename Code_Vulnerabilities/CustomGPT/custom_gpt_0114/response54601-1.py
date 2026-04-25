
def count_lines_after_key(fname, key):
    with open(fname) as f:
        found_key = False
        line_count = 0

        for line in f:
            if found_key:
                line_count += 1
            if key in line:
                found_key = True

    return line_count

# Usage
file_name = "test.ghx"
key_line = "{A   B}"
lines_after = count_lines_after_key(file_name, key_line)
print("Number of lines after '{}': {}".format(key_line, lines_after))
