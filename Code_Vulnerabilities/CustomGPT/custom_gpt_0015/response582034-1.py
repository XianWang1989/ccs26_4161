
class MyIterator:
    def __init__(self, loop_iterable):
        self.loop_iterable = loop_iterable
        self.iterator = iter(loop_iterable)
        self.enter_loop()

    def enter_loop(self):
        print("Entering the loop.")

    def __iter__(self):
        return self

    def __next__(self):
        try:
            self.loop_start()
            value = next(self.iterator)
            return value
        except StopIteration:
            self.exit_loop()
            raise

    def loop_start(self):
        print("Starting loop iteration.")

    def loop_end(self):
        print("Ending loop iteration.")

    def exit_loop(self):
        print("Exiting the loop.")

    def __next__(self):
        try:
            self.loop_start()
            value = next(self.iterator)  # Get the next item
            self.loop_end()  # End the current iteration
            return value
        except StopIteration:
            self.exit_loop()
            raise


# Example usage
for i in MyIterator([1, 2, 3]):
    print("i:", i)
    if i == 2:
        break  # This will now call exit_loop()
