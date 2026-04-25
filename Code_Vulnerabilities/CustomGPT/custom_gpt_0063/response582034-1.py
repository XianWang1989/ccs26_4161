
class MyIterator:
    def __init__(self, loop_iterable):
        self.loop_iterable = iter(loop_iterable)
        self.started = False

    def enter_loop(self):
        print("Entering loop")

    def loop_start(self):
        print("Loop start")

    def loop_end(self):
        print("Loop end")

    def exit_loop(self):
        print("Exiting loop")

    def __iter__(self):
        self.enter_loop()
        return self

    def __next__(self):
        if not self.started:
            self.started = True

        try:
            self.loop_start()
            value = next(self.loop_iterable)
            return value
        finally:
            self.loop_end()

    def close(self):
        self.exit_loop()


# Using the MyIterator class
try:
    for i in MyIterator([1, 2, 3]):
        print("i:", i)
        if i == 2:
            break  # Loop exits here
finally:
    # Ensure exit_loop() is called
    MyIterator([1, 2, 3]).close()
