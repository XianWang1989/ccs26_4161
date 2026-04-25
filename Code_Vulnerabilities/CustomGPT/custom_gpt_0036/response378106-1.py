
class FileEditor:
    def __init__(self, filename):
        self.file = filename
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        t = self.f.tell()  # Save the current position
        self.f.seek(0)     # Move to the beginning of the file
        lines = self.f.readlines()  # Read all lines into a list
        lc = 0              # Line count

        # now iterate over the lines
        for line in lines:
            if t >= len(line):
                t -= len(line)
                lc += 1
            else:
                break

        if char:
            return lc, t
        return lc

    def close(self):
        self.f.close()

# Example usage
if __name__ == '__main__':
    editor = FileEditor('example.txt')
    # You would put some text in the file first to test with
    editor.f.write("First line\nSecond line\nThird line\n")
    editor.f.flush()  # Ensure all data is written before calling tell()

    line_count = editor.tell()  # Retrieve the line count
    print(f"Number of lines counted: {line_count}")

    editor.close()  # Don't forget to close the file
