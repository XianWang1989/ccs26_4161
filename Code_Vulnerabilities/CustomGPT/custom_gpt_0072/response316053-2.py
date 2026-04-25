
class Clock:
    def __init__(self, parent, name, format_str):
        self.parent = parent
        self.format = format_str
        self.name = name

    def update(self):
        current_time = time.strftime(self.format)
        print("Updating clock to", current_time)
        self.parent.runFromChildToParent(current_time)
