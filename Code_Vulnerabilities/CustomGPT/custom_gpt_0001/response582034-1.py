
class MyFor:
    def __init__(self, loop_iterable):
        self.loop_iterable = loop_iterable
        self.iterator = iter(loop_iterable)

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
        print("Entering loop")

    def loop_start(self):
        print("Loop start")

    def loop_end(self):
        print("Loop end")

    def exit_loop(self):
        print("Exiting loop")

# Usage
for i in MyFor([1, 2, 3]):
    print("i:", i)
    if i == 2:
        break  # Will automatically call loop_end() and exit_loop()
