
class MyFor:
    def __init__(self, loop_iterable):
        self.loop_iterable = loop_iterable
        self.iterator = iter(loop_iterable)
        self.enter_loop()

    def enter_loop(self):
        print("Entering the loop")

    def loop_start(self):
        print("Loop start")

    def loop_end(self):
        print("Loop end")

    def exit_loop(self):
        print("Exiting the loop")

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
            # Ensure cleanup happens on break
            if self.iterator is not None and self.iterator is not iter(self.loop_iterable):
                self.loop_end()

# Usage
for i in MyFor([1, 2, 3]):
    print("i:", i)
    if i == 2:
        break  # loop_end() and exit_loop() execute automatically
