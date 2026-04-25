
def count_lines_after_specific_line(fname, target_line):
    count = 0
    found = False

    with open(fname) as f:
        for line in f:
            if found:
                count += 1
            if target_line in line:
                found = True

    return count

# Specify the file name and the line to search for
file_name = "test.ghx"
target = "{A   B}"
lines_count = count_lines_after_specific_line(file_name, target)

print(f'Number of lines after "{target}": {lines_count}')
