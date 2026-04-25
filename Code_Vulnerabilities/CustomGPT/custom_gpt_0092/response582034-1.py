
class MyForIterator:
    def __init__(self, iterable):
        self.iterable = iterable
        self.index = 0
        self.enter_loop()

    def enter_loop(self):
        print("Entered loop")

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.iterable):
            self.exit_loop()
            raise StopIteration

        self.loop_start()
        value = self.iterable[self.index]
        self.index += 1
        self.loop_end()
        return value

    def loop_start(self):
        print(f"Loop start for index {self.index}")

    def loop_end(self):
        print(f"Loop end for index {self.index - 1}")

    def exit_loop(self):
        print("Exited loop")

# Usage
iterator = MyForIterator([1, 2, 3])
for i in iterator:
    print("i:", i)
    if i == 2:
        break
