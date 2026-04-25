
class MyFor:
    def __init__(self, loop_iterable):
        self.loop_iterable = loop_iterable
        self.iterator = iter(loop_iterable)

    def enter_loop(self):
        print("Entered loop")

    def loop_start(self):
        print("Loop start")

    def loop_end(self):
        print("Loop end")

    def exit_loop(self):
        print("Exited loop")

    def __iter__(self):
        self.enter_loop()
        return self

    def __next__(self):
        self.loop_start()
        try:
            value = next(self.iterator)
            return value
        except StopIteration:
            self.exit_loop()
            raise

    def __del__(self):
        self.exit_loop()

# Usage
for i in MyFor([1, 2, 3]):
    print("i:", i)
    if i == 2:
        break
