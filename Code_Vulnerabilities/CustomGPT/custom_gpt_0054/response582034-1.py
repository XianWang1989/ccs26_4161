
class CustomIterator:
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
        finally:
            self.loop_end()

    def loop_start(self):
        print("Starting loop iteration.")

    def loop_end(self):
        print("Ending loop iteration.")

    def exit_loop(self):
        print("Exiting the loop.")

# Use a context manager to ensure exit_loop is called after the loop ends
from contextlib import contextmanager

@contextmanager
def custom_loop(loop_iterable):
    iterator = CustomIterator(loop_iterable)
    try:
        yield iterator
    finally:
        iterator.exit_loop()

# Usage
with custom_loop([1, 2, 3]) as loop:
    for i in loop:
        print("i:", i)
        if i == 2:
            break
