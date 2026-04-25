
class MyForIterator:
    def __init__(self, loop_iterable):
        self.loop_iterable = iter(loop_iterable)
        self.iteration_started = False
        self.enter_loop()

    def enter_loop(self):
        print("Entering loop...")

    def loop_start(self):
        print("Starting loop iteration...")

    def loop_end(self):
        print("Ending loop iteration...")

    def exit_loop(self):
        print("Exiting loop...")

    def __iter__(self):
        return self

    def __next__(self):
        try:
            item = next(self.loop_iterable)
            if not self.iteration_started:
                self.iteration_started = True
            self.loop_start()
            return item
        except StopIteration:
            self.exit_loop()
            raise

    def __del__(self):
        if self.iteration_started:
            self.exit_loop()

# Using the custom iterator
for i in MyForIterator([1, 2, 3]):
    print("i:", i)
    if i == 2:
        break
    print("Processed:", i)
