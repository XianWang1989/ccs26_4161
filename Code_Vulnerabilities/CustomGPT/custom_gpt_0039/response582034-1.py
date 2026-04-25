
class CustomIterator:
    def __init__(self, loop_iterable):
        self.iterable = iter(loop_iterable)
        self.enter_loop()

    def enter_loop(self):
        print("Entering loop...")

    def exit_loop(self):
        print("Exiting loop...")

    def loop_start(self):
        print("Loop start...")

    def loop_end(self):
        print("Loop end...")

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

    def close(self):
        self.loop_end()
        self.exit_loop()

# Usage
iterator = CustomIterator([1, 2, 3])
try:
    for i in iterator:
        print("i:", i)
        if i == 2:
            break  # The loop ends here
finally:
    iterator.close()  # Ensure cleanup happens here
