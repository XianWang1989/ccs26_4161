
class FileEditor:
    def __init__(self, filename):
        self.file = filename
        self.f = open(self.file, 'a+')

    def tell(self, char=False):
        current_position = self.f.tell()
        self.f.seek(0)  # Go to the start of the file

        line_count = 0
        char_position = current_position

        while True:
            line = self.f.readline()
            if not line:  # EOF
                break
            if char_position <= len(line):
                break
            char_position -= len(line)
            line_count += 1

        self.f.seek(current_position)  # Restore to original position

        if char:
            return line_count, char_position
        return line_count

    def close(self):
        self.f.close()
