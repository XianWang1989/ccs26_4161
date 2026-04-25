
class MyFor:
    def __init__(self, loop_iterable):
        self.loop_iterable = loop_iterable
        self.iterator = iter(loop_iterable)
        self.loop_active = True
        self.enter_loop()

    def enter_loop(self):
        print("Entering loop")

    def loop_start(self):
        print("Loop start")

    def loop_end(self):
        print("Loop end")

    def exit_loop(self):
        print("Exiting loop")

    def __iter__(self):
        return self

    def __next__(self):
        if not self.loop_active:
            self.exit_loop()
            raise StopIteration

        try:
            value = next(self.iterator)
        except StopIteration:
            self.loop_active = False
            self.exit_loop()
            raise

        self.loop_start()
        return value

    def __broke__(self):
        self.loop_end()
        self.loop_active = False

# Usage
my_loop = MyFor([1, 2, 3])
for i in my_loop:
    print("i:", i)
    if i == 2:
        my_loop.__broke__()  # Simulate break behavior
        break
