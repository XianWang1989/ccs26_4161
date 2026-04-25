
def tell(self, char=False):
    t = self.f.tell()  # Get the current position
    self.f.seek(0)  # Go back to the start of the file

    lines = self.f.readlines()  # Read all lines into a list
    lc = 0  # Line counter

    for line in lines:
        if t >= len(line):  # Check the current position against line lengths
            t -= len(line)
            lc += 1
        else:
            break

    self.f.seek(t)  # Reset the pointer back to the original position
    if char:
        return lc, t
    return lc

# Example usage:
with open('example.txt', 'a+') as f:
    f.write("First line\nSecond line\nThird line\n")
    f.seek(0)  # Reset the file pointer to the start
    my_file = MyFileClass(f)
    print(my_file.tell())
