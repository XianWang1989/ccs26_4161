
class FileEditor:
    def __init__(self, filename):
        self.file = filename
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        t = self.f.tell()
        self.f.seek(0)

        line_count = 0
        byte_count = 0

        while True:
            line = self.f.readline()
            if not line:  # End of file
                break

            if byte_count + len(line) > t:
                break

            byte_count += len(line)
            line_count += 1

        self.f.seek(t)  # Restore the original position

        if char:
            return line_count, t - byte_count  # Return line count and column index in the line
        return line_count

    def close(self):
        self.f.close()

# Example usage:
editor = FileEditor('example.txt')
line_number = editor.tell()
print(f"Current line number: {line_number}")
editor.close()
