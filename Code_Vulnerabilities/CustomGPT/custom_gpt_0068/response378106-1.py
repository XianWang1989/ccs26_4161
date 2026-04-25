
class FileEditor:
    def __init__(self, filename):
        self.file = filename
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        # Save the current position
        t = self.f.tell()  # Get the current byte position
        self.f.seek(0)     # Move to the beginning of the file

        lc = 0
        accumulated_length = 0
        for line in self.f:
            line_length = len(line)
            if accumulated_length + line_length > t:  # Check if t falls within this line
                t -= accumulated_length  # Calculate byte position within this line
                break
            accumulated_length += line_length
            lc += 1

        self.f.seek(t + accumulated_length)  # Restore pointer to original position
        if char:
            return lc, t
        return lc

    def close(self):
        self.f.close()

# Example Usage
editor = FileEditor('example.txt')
line_count = editor.tell()
print(f'The line count is: {line_count}')
editor.close()
