
class MyIterator:
    def __init__(self, loop_iterable):
        self.loop_iterable = iter(loop_iterable)
        self.enter_loop()

    def enter_loop(self):
        print("Entering the loop")

    def loop_start(self):
        print("Loop starting")

    def loop_end(self):
        print("Loop ending")

    def exit_loop(self):
        print("Exiting the loop")

    def __iter__(self):
        return self

    def __next__(self):
        try:
            self.loop_start()
            value = next(self.loop_iterable)
            return value
        finally:
            self.loop_end()

    def close(self):
        self.exit_loop()

# Example usage
iterable = MyIterator([1, 2, 3])
try:
    for i in iterable:
        print("i:", i)
        if i == 2:
            break  # This will still trigger the loop end and exit
finally:
    iterable.close()
