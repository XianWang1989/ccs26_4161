
class MyFor:
    def __init__(self, loop_iterable):
        self.loop_iterable = loop_iterable
        self.index = 0
        self.enter_loop()

    def enter_loop(self):
        print("Entered the loop.")

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.loop_iterable):
            self.exit_loop()
            raise StopIteration

        loop_start_result = self.loop_start()
        item = self.loop_iterable[self.index]
        self.index += 1
        self.loop_end()
        return item

    def loop_start(self):
        print("Loop starting...")

    def loop_end(self):
        print("Loop ended.")

    def exit_loop(self):
        print("Exited the loop.")

# Using the custom iterator
for i in MyFor([1, 2, 3]):
    print("i:", i)
    if i == 2:
        break  # loop_end() and exit_loop() will be called automatically
