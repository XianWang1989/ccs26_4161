
class CustomIterator:
    def __init__(self, loop_iterable):
        self.loop_iterable = loop_iterable
        self.iterator = iter(loop_iterable)
        self.enter_loop()

    def __iter__(self):
        return self

    def __next__(self):
        try:
            loop_start()
            value = next(self.iterator)
            loop_end()
            return value
        except StopIteration:
            self.exit_loop()
            raise

    def enter_loop(self):
        print("Entering the loop.")

    def loop_start(self):
        print("Loop started.")

    def loop_end(self):
        print("Loop ended.")

    def exit_loop(self):
        print("Exiting the loop.")

for i in CustomIterator([1, 2, 3]):
    print("i:", i)
    if i == 2:
        break
