
class MyFor:
    def __init__(self, iterable):
        self.iterable = iterable

    def __enter__(self):
        self.enter_loop()
        return self

    def __iter__(self):
        for item in self.iterable:
            self.loop_start()
            yield item
            self.loop_end()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.exit_loop()

    def enter_loop(self):
        print("Entering the loop...")

    def loop_start(self):
        print("Loop iteration starting...")

    def loop_end(self):
        print("Loop iteration ending...")

    def exit_loop(self):
        print("Exiting the loop...")


# Using the custom iterator
with MyFor([1, 2, 3]) as my_iterator:
    for i in my_iterator:
        print("i: ", i)
        if i == 2:
            break  # This will ensure exit_loop() is called.
