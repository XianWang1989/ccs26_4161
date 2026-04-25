
class MyFor:
    def __init__(self, loop_iterable):
        self.loop_iterable = loop_iterable
        self.iterator = iter(loop_iterable)
        self.enter_loop()

    def enter_loop(self):
        print("Entering the loop")

    def loop_start(self):
        print("Loop start")

    def loop_end(self):
        print("Loop end")

    def exit_loop(self):
        print("Exiting the loop")

    def __iter__(self):
        return self

    def __next__(self):
        try:
            self.loop_start()
            value = next(self.iterator)
            return value
        finally:
            self.loop_end()  # Ensures loop_end is called every iteration

    def __del__(self):
        self.exit_loop()  # Ensures exit_loop is called on iterator destruction

# Usage
for i in MyFor([1, 2, 3]):
    print("i:", i)
    if i == 2:
        break
