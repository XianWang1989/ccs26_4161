
class MyFor:
    def __init__(self, loop_iterable):
        self.loop_iterable = loop_iterable
        self.index = 0
        self.enter_loop()

    def enter_loop(self):
        print("Entering loop...")

    def loop_start(self):
        print("Loop start...")

    def loop_end(self):
        print("Loop end...")

    def exit_loop(self):
        print("Exiting loop...")

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.loop_iterable):
            self.exit_loop()
            raise StopIteration

        self.loop_start()
        value = self.loop_iterable[self.index]
        self.index += 1
        self.loop_end()
        return value

    def __del__(self):
        # Called when the instance is deleted or garbage collected
        self.exit_loop()


# Example usage
my_iter = MyFor([1, 2, 3])
for i in my_iter:
    print("i:", i)
    if i == 2:
        break  # The `loop_end` and `exit_loop` will still execute
