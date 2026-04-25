
class MyIterator:
    def __init__(self, loop_iterable):
        self.loop_iterable = loop_iterable
        self.index = 0
        self.enter_loop()

    def enter_loop(self):
        print("Entering loop")

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.loop_iterable):
            # Loop start logic
            print("Loop start")
            value = self.loop_iterable[self.index]
            self.index += 1
            return value
        else:
            self.exit_loop()
            raise StopIteration

    def exit_loop(self):
        print("Exiting loop")

    def loop_end(self):
        print("Loop end")

# Using the custom iterator
for i in MyIterator([1, 2, 3]):
    print("i:", i)
    if i == 2:
        # Instead of a break, we simply raise StopIteration
        # This will trigger the exit logic appropriately
        raise StopIteration
    print("After loop end")  # This won't execute after a break
