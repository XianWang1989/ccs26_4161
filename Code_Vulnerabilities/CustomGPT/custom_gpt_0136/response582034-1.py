
class MyFor:
    def __init__(self, loop_iterable):
        self.loop_iterable = loop_iterable
        self.iterator = iter(loop_iterable)
        self.started = False

    def enter_loop(self):
        print("Entering loop.")

    def loop_start(self):
        print("Loop start.")

    def loop_end(self):
        print("Loop end.")

    def exit_loop(self):
        print("Exiting loop.")

    def __iter__(self):
        self.enter_loop()
        self.started = True
        return self

    def __next__(self):
        if self.started:
            try:
                self.loop_start()
                value = next(self.iterator)
                return value
            finally:
                self.loop_end()  # This will run unless an exception occurs
        raise StopIteration

    def __del__(self):
        if self.started:
            self.exit_loop()

# Usage
for i in MyFor([1, 2, 3]):
    print("i:", i)
    if i == 2:
        break
