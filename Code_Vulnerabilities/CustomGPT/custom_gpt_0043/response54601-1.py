
def count_lines_after_specific(fname, specific_line):
    with open(fname, 'r') as f:
        after_count = False  # Flag to indicate if we have found the specific line
        count = 0  # Counter for lines after the specific line

        for line in f:
            if after_count:
                count += 1  # Increment the count for every line after the specific line
            if specific_line in line:
                after_count = True  # We found the specific line, start counting

    return count

# Example usage
filename = "test.ghx"  # Replace this with your actual file name
specific_line = "{A   B}"

line_count = count_lines_after_specific(filename, specific_line)
print("Number of lines after '{}': {}".format(specific_line, line_count))
