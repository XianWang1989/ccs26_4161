
class CustomIterator:
    def __init__(self, loop_iterable):
        self.loop_iterable = loop_iterable
        self.iterator = iter(loop_iterable)

    def enter_loop(self):
        print("Entering loop")

    def loop_start(self):
        print("Loop start")

    def loop_end(self):
        print("Loop end")

    def exit_loop(self):
        print("Exiting loop")

    def __iter__(self):
        self.enter_loop()
        return self

    def __next__(self):
        try:
            item = next(self.iterator)
            self.loop_start()
            return item
        except StopIteration:
            self.exit_loop()
            raise

    def next_item(self):
        try:
            item = next(self.iterator)
            self.loop_end()
            return item
        except StopIteration:
            self.exit_loop()
            raise

# Usage
for i in CustomIterator([1, 2, 3]):
    print("i:", i)
    if i == 2:
        break
