
class MyIterator:
    def __init__(self, loop_iterable):
        self.loop_iterable = loop_iterable
        self.iterator = iter(loop_iterable)
        self.enter_loop()

    def enter_loop(self):
        print("Entering loop...")

    def __iter__(self):
        return self

    def __next__(self):
        try:
            self.loop_start()
            next_item = next(self.iterator)
            return next_item
        except StopIteration:
            self.exit_loop()
            raise

    def loop_start(self):
        print("Loop started...")

    def loop_end(self):
        print("Loop ended...")

    def exit_loop(self):
        print("Exiting loop...")

    def __del__(self):
        # Ensure cleanup if the iterator is deleted or goes out of scope
        self.exit_loop()

# Usage
for i in MyIterator([1, 2, 3]):
    print("i:", i)
    if i == 2:
        break  # loop_end() and exit_loop() will still execute
