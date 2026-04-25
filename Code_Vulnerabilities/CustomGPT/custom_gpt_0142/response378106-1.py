
class FileEditor:
    def __init__(self, file):
        self.file = file
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        t = self.f.tell()  # Get the current byte position
        self.f.seek(0)  # Go to the start of the file
        lines = self.f.readlines()  # Read all lines into a list
        lc = 0  # Line count

        for line in lines:
            if t >= len(line):  # Compare current position with line length
                t -= len(line)  # Subtract the length of the line from t
                lc += 1  # Increment line count
            else:
                break  # Exit if current position falls within the line

        self.f.seek(t)  # Reset to the original position
        if char:
            return lc, t
        return lc

    def close(self):
        self.f.close()

# Example usage
file_editor = FileEditor('example.txt')
line_count = file_editor.tell()  # Get the line count only
print(f'Current line count: {line_count}')
file_editor.close()
