
def count_lines_after_specified_line(fname, specified_line):
    with open(fname) as f:
        found = False
        count = 0
        for line in f:
            if found:
                count += 1
            if specified_line in line:
                found = True
    return count

# Example usage
filename = "test.ghx"
specified_line = "{A   B}"
result = count_lines_after_specified_line(filename, specified_line)
print(result)
