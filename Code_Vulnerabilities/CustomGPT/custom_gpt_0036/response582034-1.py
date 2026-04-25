
class CustomIterator:
    def __init__(self, loop_iterable):
        self.loop_iterable = loop_iterable
        self.iterator = iter(loop_iterable)
        self.enter_loop()

    def enter_loop(self):
        print("Entering loop.")

    def loop_start(self):
        print("Loop start.")

    def loop_end(self):
        print("Loop end.")

    def exit_loop(self):
        print("Exiting loop.")

    def __iter__(self):
        return self

    def __next__(self):
        try:
            value = next(self.iterator)
            self.loop_start()
            return value
        finally:
            self.loop_end()

    def close(self):
        self.exit_loop()

# Usage of CustomIterator
custom_iter = CustomIterator([1, 2, 3])
try:
    for i in custom_iter:
        print("i:", i)
        if i == 2:
            break  # Loop will end here, but cleanup will still happen.
finally:
    custom_iter.close()  # Ensure exit_loop() is called.
