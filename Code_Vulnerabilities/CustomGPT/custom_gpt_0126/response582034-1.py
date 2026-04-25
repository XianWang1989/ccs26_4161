
class MyIterator:
    def __init__(self, loop_iterable):
        self.loop_iterable = loop_iterable
        self.iterator = iter(loop_iterable)
        self.loop_enter()

    def loop_enter(self):
        print("Entering loop.")

    def loop_start(self):
        print("Starting a new loop iteration.")

    def loop_end(self):
        print("Ending the loop iteration.")

    def exit_loop(self):
        print("Exiting loop.")

    def __iter__(self):
        return self

    def __next__(self):
        try:
            item = next(self.iterator)
            self.loop_start()
            return item
        finally:
            self.loop_end()  # Ensures this runs whether __next__ is successful or raises StopIteration

    def __del__(self):
        self.exit_loop()  # Ensures cleanup on deletion of iterator


# Usage
iterator = MyIterator([1, 2, 3])
for i in iterator:
    print("i:", i)
    if i == 2:
        break  # Loop cleanup will occur here automatically
