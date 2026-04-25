
class CustomIterator:
    def __init__(self, loop_iterable):
        self.loop_iterable = loop_iterable
        self.index = 0
        self.started = False

    def enter_loop(self):
        print("Entering loop...")

    def loop_start(self):
        print("Loop start...")

    def loop_end(self):
        print("Loop end...")

    def exit_loop(self):
        print("Exiting loop...")

    def __iter__(self):
        self.enter_loop()
        return self

    def __next__(self):
        if self.index >= len(self.loop_iterable):
            self.exit_loop()
            raise StopIteration
        item = self.loop_iterable[self.index]
        self.loop_start()
        self.index += 1
        self.loop_end()
        return item

# Usage:
for i in CustomIterator([1, 2, 3]):
    print("i:", i)
    if i == 2:
        break
