
def count_lines_after_marker(fname, marker):
    with open(fname) as f:
        lines = f.readlines()  # Read all lines into a list
        found_marker = False
        count = 0

        for line in lines:
            if found_marker:
                count += 1  # Count lines after the marker
            if marker in line:
                found_marker = True  # Once the marker is found, start counting

    return count

# Define your marker
marker = '{A   B}'
# Call the function and print the result
num_lines = count_lines_after_marker("test.ghx", marker)
print(f"Number of lines after the marker '{marker}': {num_lines}")
