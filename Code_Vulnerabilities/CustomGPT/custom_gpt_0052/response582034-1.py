
class MyFor:
    def __init__(self, loop_iterable):
        self.loop_iterable = iter(loop_iterable)
        self.has_ended = False
        self.enter_loop()

    def enter_loop(self):
        print("Entering loop")

    def __iter__(self):
        return self

    def __next__(self):
        if self.has_ended:
            raise StopIteration
        try:
            self.loop_start()
            item = next(self.loop_iterable)
            return item
        finally:
            self.loop_end()

    def loop_start(self):
        print("Loop starts")

    def loop_end(self):
        print("Loop ends")

    def exit_loop(self):
        print("Exiting loop")
        self.has_ended = True

    def __del__(self):
        if not self.has_ended:
            self.exit_loop()

# Usage
for i in MyFor([1, 2, 3]):
    print("i:", i)
    if i == 2:
        break  # Cleanup happens automatically
