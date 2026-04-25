
class MyFor:
    def __init__(self, loop_iterable):
        self.loop_iterable = loop_iterable
        self.iterator = iter(loop_iterable)
        self.is_exited = False
        self.enter_loop()

    def enter_loop(self):
        print("Entering loop.")

    def loop_start(self):
        print("Loop starts.")

    def loop_end(self):
        print("Loop ends.")

    def exit_loop(self):
        self.is_exited = True
        print("Exiting loop.")

    def __iter__(self):
        return self

    def __next__(self):
        if self.is_exited:
            raise StopIteration
        try:
            self.loop_start()
            value = next(self.iterator)
            self.loop_end()
            return value
        except StopIteration:
            self.exit_loop()
            raise

# Usage
for i in MyFor([1, 2, 3]):
    print("i:", i)
    if i == 2:
        break
