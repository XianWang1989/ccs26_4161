
class CustomIterator:
    def __init__(self, loop_iterable):
        self.loop_iterable = iter(loop_iterable)
        self.finished = False
        self.enter_loop()

    def enter_loop(self):
        print("Entered loop")

    def __iter__(self):
        return self

    def __next__(self):
        if self.finished:
            self.exit_loop()
            raise StopIteration

        try:
            item = next(self.loop_iterable)
            self.loop_start()
            return item
        except StopIteration:
            self.finished = True
            self.exit_loop()
            raise

    def loop_start(self):
        print("Loop start")

    def loop_end(self):
        print("Loop end")

    def exit_loop(self):
        print("Exited loop")


for i in CustomIterator([1, 2, 3]):
    print("i:", i)
    if i == 2:
        break
