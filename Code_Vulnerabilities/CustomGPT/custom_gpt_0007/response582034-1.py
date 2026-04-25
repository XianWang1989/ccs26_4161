
class MyIterator:
    def __init__(self, loop_iterable):
        self.loop_iterable = loop_iterable
        self.iterator = iter(loop_iterable)
        self.is_finished = False
        self.enter_loop()

    def enter_loop(self):
        print("Entering the loop.")

    def loop_start(self):
        print("Loop started.")

    def loop_end(self):
        print("Loop ended.")

    def exit_loop(self):
        print("Exiting the loop.")

    def __iter__(self):
        return self

    def __next__(self):
        if self.is_finished:
            self.exit_loop()
            raise StopIteration

        try:
            self.loop_start()
            value = next(self.iterator)
            return value
        except StopIteration:
            self.is_finished = True
            self.exit_loop()
            raise

        self.loop_end()

# Usage
for i in MyIterator([1, 2, 3]):
    print("i: ", i)
    if i == 2:
        # Automatically handle loop end and exit on break
        break
