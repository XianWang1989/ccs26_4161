
class MyIterator:
    def __init__(self, loop_iterable):
        self.loop_iterable = loop_iterable
        self.index = 0
        self.enter_loop()

    def enter_loop(self):
        print("Entering loop")

    def loop_start(self):
        print(f"Starting loop iteration {self.index + 1}")

    def loop_end(self):
        print(f"Ending loop iteration {self.index + 1}")

    def exit_loop(self):
        print("Exiting loop")

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.loop_iterable):
            self.exit_loop()
            raise StopIteration

        self.loop_start()
        value = self.loop_iterable[self.index]
        self.index += 1
        self.loop_end()
        return value


# Usage
for i in MyIterator([1, 2, 3]):
    print("i:", i)
    if i == 2:
        break  # loop_end() and exit_loop() are called automatically after the break
