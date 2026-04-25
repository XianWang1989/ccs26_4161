class MyForIterator:
    def __init__(self, loop_iterable):
        self.loop_iterable = loop_iterable
        self.iterator = iter(loop_iterable)
        self.finished = False
        enter_loop()

    def __iter__(self):
        return self

    def __next__(self):
        if self.finished:
            raise StopIteration
        try:
            # Loop start logic
            loop_start()
            # Get next item from the iterable
            item = next(self.iterator)
            return item
        except StopIteration:
            # End of iteration
            self.finished = True
            loop_end()
            exit_loop()
            raise StopIteration

    def __del__(self):
        if not self.finished:
            loop_end()
            exit_loop()

def enter_loop():
    print("Entering the loop")

def loop_start():
    print("Loop started")

def loop_end():
    print("Loop ended")

def exit_loop():
    print("Exiting the loop")

# Using the custom iterator
for i in MyForIterator([1, 2, 3]):
    print(f"i: {i}")
    if i == 2:
        break
