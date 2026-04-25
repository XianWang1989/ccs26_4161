
class MyFor:
    def __init__(self, loop_iterable):
        self.loop_iterable = loop_iterable

    def __iter__(self):
        self.enter_loop()
        for i in self.loop_iterable:
            self.loop_start()
            yield i
            self.loop_end()
        self.exit_loop()

    def enter_loop(self):
        print("Entering the loop.")

    def loop_start(self):
        print("Starting loop iteration.")

    def loop_end(self):
        print("Ending loop iteration.")

    def exit_loop(self):
        print("Exiting the loop.")


# Using the custom iterator
my_iterator = MyFor([1, 2, 3])
try:
    for i in my_iterator:
        print("i: ", i)
        if i == 2:
            raise StopIteration  # Mimics a break
except StopIteration:
    my_iterator.exit_loop()  # Ensures exit_loop runs after a break
