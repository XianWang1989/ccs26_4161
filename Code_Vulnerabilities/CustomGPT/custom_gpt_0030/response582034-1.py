
class MyIterator:
    def __init__(self, loop_iterable):
        self.iterable = loop_iterable
        self.iterator = iter(loop_iterable)
        self.enter_loop()

    def enter_loop(self):
        print("Entering loop...")

    def loop_start(self):
        print("Loop iteration start...")

    def loop_end(self):
        print("Loop iteration end...")

    def exit_loop(self):
        print("Exiting loop...")

    def __iter__(self):
        return self

    def __next__(self):
        try:
            self.loop_start()
            value = next(self.iterator)
            self.loop_end()
            return value
        except StopIteration:
            self.exit_loop()
            raise

# Usage example
for i in MyIterator([1, 2, 3]):
    print("i:", i)
    if i == 2:
        break  # This will now properly call exit_loop()
