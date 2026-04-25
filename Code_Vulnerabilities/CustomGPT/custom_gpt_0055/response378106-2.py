
with open('example.txt', 'a+') as f:
    # Write sample lines
    f.write('First line.\nSecond line.\nThird line.\n')
    f.flush()

    f.seek(0)  # Go back to the beginning for example
    my_file = YourClass(file='example.txt')
    line_count = my_file.tell()  # Get line count
    print("Line count:", line_count)
