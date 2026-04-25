
class MyFor:
    def __init__(self, loop_iterable):
        self.loop_iterable = loop_iterable
        self.index = 0

        # Call to enter_loop on instantiation
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
        if self.index < len(self.loop_iterable):
            self.loop_start()
            item = self.loop_iterable[self.index]
            self.index += 1
            return item
        else:
            self.exit_loop()
            raise StopIteration

# Using the custom iterator
for i in MyFor([1, 2, 3]):
    print("i:", i)
    if i == 2:
        # Exit the loop but still call loop_end and exit_loop
        break
    print("Looping...")
