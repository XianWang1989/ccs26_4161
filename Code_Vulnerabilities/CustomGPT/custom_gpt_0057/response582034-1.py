
class CustomIterator:
    def __init__(self, loop_iterable):
        self.iterable = iter(loop_iterable)
        self.done = False
        self.enter_loop()

    def enter_loop(self):
        print("Entering loop.")

    def loop_start(self):
        print("Loop start.")

    def loop_end(self):
        print("Loop end.")

    def exit_loop(self):
        print("Exiting loop.")
        self.done = True

    def __iter__(self):
        return self

    def __next__(self):
        if self.done:
            raise StopIteration
        self.loop_start()
        try:
            value = next(self.iterable)
            return value
        finally:
            self.loop_end()

    def __del__(self):
        if not self.done:
            self.exit_loop()

for i in CustomIterator([1, 2, 3]):
    print("i:", i)
    if i == 2:
        break
