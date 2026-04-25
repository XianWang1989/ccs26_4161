
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
        # Start of loop logic
        self.loop_start()
        try:
            value = next(self.iterator)
            return value
        except StopIteration:
            self.exit_loop()
            raise

    def loop_start(self):
        print("Loop start...")

    def loop_end(self):
        print("Loop end...")

    def exit_loop(self):
        print("Exiting loop...")

    def __del__(self):
        self.exit_loop()  # Ensure exit_loop is called on deletion

# Usage
for i in MyIterator([1, 2, 3]):
    print("i:", i)
    if i == 2:
        break  # Loop ends gracefully, and exit_loop will still be called
