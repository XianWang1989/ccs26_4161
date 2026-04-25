
class MyIterator:
    def __init__(self, iterable):
        self.iterable = iterable
        self.iter = iter(iterable)

    def __iter__(self):
        self.enter_loop()
        return self

    def __next__(self):
        try:
            self.loop_start()
            value = next(self.iter)
            self.loop_end()
            return value
        except StopIteration:
            self.exit_loop()
            raise

    def enter_loop(self):
        print("Entering the loop.")

    def loop_start(self):
        print("Starting a new iteration.")

    def loop_end(self):
        print("Ending the iteration.")

    def exit_loop(self):
        print("Exiting the loop.")

# Usage example
for i in MyIterator([1, 2, 3]):
    print("i:", i)
    if i == 2:
        break
