
class CustomIterator:
    def __init__(self, loop_iterable):
        self.loop_iterable = loop_iterable
        self.iterator = iter(loop_iterable)
        self.started = False

    def enter_loop(self):
        print("Entering loop.")

    def loop_start(self):
        print("Start of loop iteration.")

    def loop_end(self):
        print("End of loop iteration.")

    def exit_loop(self):
        print("Exiting loop.")

    def __iter__(self):
        self.enter_loop()
        return self

    def __next__(self):
        if not self.started:
            self.started = True
        try:
            value = next(self.iterator)
            self.loop_start()
            return value
        except StopIteration:
            self.exit_loop()
            raise

    def close(self):
        # Clean-up action
        self.exit_loop()


# Usage
custom_iterator = CustomIterator([1, 2, 3])
for i in custom_iterator:
    print("i:", i)
    if i == 2:
        custom_iterator.loop_end()  # Ensure this is called
        custom_iterator.exit_loop()  # Ensure this is called
        break
