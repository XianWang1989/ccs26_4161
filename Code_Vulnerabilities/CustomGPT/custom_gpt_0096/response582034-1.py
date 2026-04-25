
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
            value = next(self.iterator)
            return value
        finally:
            self.loop_end()

    def loop_start(self):
        print("Loop starting...")

    def loop_end(self):
        print("Loop ending...")

    def exit_loop(self):
        print("Exiting loop...")

    def __del__(self):
        self.exit_loop()

# Usage
for i in MyIterator([1, 2, 3]):
    print("i:", i)
    if i == 2:
        break  # Cleanup will still happen
