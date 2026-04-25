
with open('example.txt', 'a+') as f:
    f.write("First line\nSecond line\nThird line\n")
    f.seek(0)  # Go back to the start for testing
    my_instance = MyClass(f)  # Assuming your class is named MyClass
    line_count = my_instance.tell()
    print(f"Line count: {line_count}")  # Outputs the number of lines
