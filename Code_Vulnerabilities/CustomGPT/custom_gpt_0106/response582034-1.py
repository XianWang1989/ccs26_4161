
class MyFor:
    def __init__(self, loop_iterable):
        self.iterable = iter(loop_iterable)
        self.enter_loop()

    def enter_loop(self):
        print("Entering loop...")

    def __iter__(self):
        return self

    def __next__(self):
        try:
            self.loop_start()
            value = next(self.iterable)
            return value
        finally:
            self.loop_end()

    def loop_start(self):
        print("Loop start...")

    def loop_end(self):
        print("Loop end...")

    def exit_loop(self):
        print("Exiting loop...")

    def __del__(self):
        self.exit_loop()

# Using the custom iterator
for i in MyFor([1, 2, 3]):
    print("i:", i)
    if i == 2:
        break
