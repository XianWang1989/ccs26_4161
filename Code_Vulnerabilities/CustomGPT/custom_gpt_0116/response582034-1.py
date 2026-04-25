
class MyIterator:
    def __init__(self, iterable):
        self.iterable = iter(iterable)
        self.enter_loop()

    def enter_loop(self):
        print("Entering loop")

    def __iter__(self):
        return self

    def __next__(self):
        try:
            self.loop_start()
            value = next(self.iterable)
            return value
        except StopIteration:
            self.exit_loop()
            raise

    def loop_start(self):
        print("Loop start")

    def loop_end(self):
        print("Loop end")

    def exit_loop(self):
        print("Exiting loop")

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            self.exit_loop()  # Ensure exit on exceptions
        return False  # Propagate exceptions

# Usage
for i in MyIterator([1, 2, 3]):
    print("i:", i)
    if i == 2:
        break  # Cleanup will still happen
