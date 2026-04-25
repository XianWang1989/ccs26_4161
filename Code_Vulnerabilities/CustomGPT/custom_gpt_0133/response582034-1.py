
class CustomIterator:
    def __init__(self, iterable):
        self.iterable = iterable
        self.iterator = iter(iterable)

    def __iter__(self):
        self.enter_loop()
        return self

    def __next__(self):
        try:
            self.loop_start()
            return next(self.iterator)
        except StopIteration:
            self.exit_loop()
            raise

    def enter_loop(self):
        print("Entering the loop.")

    def loop_start(self):
        print("Loop start.")

    def loop_end(self):
        print("Loop end.")

    def exit_loop(self):
        print("Exiting the loop.")

    def close(self):
        self.exit_loop()  # Ensures cleanup regardless of how iteration stops


# Using the CustomIterator
custom_iter = CustomIterator([1, 2, 3])

try:
    for i in custom_iter:
        print("i:", i)
        if i == 2:
            break  # The exit code runs after break
except StopIteration:
    pass
finally:
    custom_iter.close()  # Ensure cleanup happens here if not via StopIteration

