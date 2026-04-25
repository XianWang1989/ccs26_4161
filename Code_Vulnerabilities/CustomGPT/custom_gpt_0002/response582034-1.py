
class MyIterator:
    def __init__(self, loop_iterable):
        self.loop_iterable = loop_iterable
        self.current = iter(loop_iterable)
        self.enter_loop()

    def enter_loop(self):
        print("Entering the loop")

    def loop_start(self):
        print("Starting loop iteration")

    def loop_end(self):
        print("Ending loop iteration")

    def exit_loop(self):
        print("Exiting the loop")

    def __iter__(self):
        return self

    def __next__(self):
        try:
            self.loop_start()
            value = next(self.current)
            return value
        except StopIteration:
            self.exit_loop()
            raise
        finally:
            self.loop_end()

for i in MyIterator([1, 2, 3]):
    print("i:", i)
    if i == 2:
        break
