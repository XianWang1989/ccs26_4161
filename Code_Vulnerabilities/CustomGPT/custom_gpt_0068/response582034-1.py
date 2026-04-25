
class MyFor:
    def __init__(self, loop_iterable):
        self.loop_iterable = loop_iterable
        self.iterator = iter(loop_iterable)
        self.enter_loop()

    def enter_loop(self):
        print("Entering loop")

    def loop_start(self):
        print("Loop started")

    def loop_end(self):
        print("Loop ended")

    def exit_loop(self):
        print("Exiting loop")

    def __iter__(self):
        return self

    def __next__(self):
        try:
            self.loop_start()
            value = next(self.iterator)
            return value
        except StopIteration:
            self.exit_loop()
            raise
        finally:
            self.loop_end()

# Usage of the custom iterator
try:
    for i in MyFor([1, 2, 3]):
        print("i:", i)
        if i == 2:
            break  # The loop_end() and exit_loop() will still execute
except StopIteration:
    pass  # Gracefully handling the end of iteration
