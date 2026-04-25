
class MyFor:
    def __init__(self, loop_iterable):
        self.loop_iterable = loop_iterable
        self.iterator = iter(loop_iterable)
        self.enter_loop()

    def enter_loop(self):
        print("Entered loop")

    def loop_start(self):
        print("Loop start")

    def loop_end(self):
        print("Loop end")

    def exit_loop(self):
        print("Exited loop")

    def __iter__(self):
        return self

    def __next__(self):
        try:
            self.loop_start()
            value = next(self.iterator)
            return value
        finally:
            self.loop_end()

    def close(self):
        self.exit_loop()

# Usage
my_for_instance = MyFor([1, 2, 3])
try:
    for i in my_for_instance:
        print("i:", i)
        if i == 2:
            break
finally:
    my_for_instance.close()
