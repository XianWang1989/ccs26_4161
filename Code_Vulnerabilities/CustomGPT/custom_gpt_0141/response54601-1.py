
def count_lines_after_marker(fname, marker):
    count = 0
    found_marker = False

    with open(fname, 'r') as f:
        for line in f:
            if found_marker:
                count += 1
            if line.strip() == marker:
                found_marker = True

    return count

# Define the marker you are looking for
marker = "{A   B}"
file_name = "test.ghx"

# Call the function and print the result
lines_count = count_lines_after_marker(file_name, marker)
print(f"The number of lines after '{marker}': {lines_count}")
