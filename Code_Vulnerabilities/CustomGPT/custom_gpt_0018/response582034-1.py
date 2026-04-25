
class MyFor:
    def __init__(self, loop_iterable):
        self.loop_iterable = iter(loop_iterable)
        self.is_done = False
        self.enter_loop()

    def enter_loop(self):
        print("Entering loop...")

    def __iter__(self):
        return self

    def __next__(self):
        if self.is_done:
            self.exit_loop()
            raise StopIteration

        # Start of loop iteration
        self.loop_start()
        try:
            value = next(self.loop_iterable)
            return value
        except StopIteration:
            self.is_done = True
            self.exit_loop()
            raise

    def loop_start(self):
        print("Loop started.")

    def loop_end(self):
        print("Loop ended.")

    def exit_loop(self):
        print("Exiting loop...")

    def __del__(self):
        if not self.is_done:
            self.exit_loop()
        print("Clean up resources...")

# Usage
my_iter = MyFor([1, 2, 3])
for i in my_iter:
    print("i:", i)
    if i == 2:
        break  # This will trigger the exit_loop cleanup
