
class MyIterator:
    def __init__(self, loop_iterable):
        self.loop_iterable = iter(loop_iterable)
        self.is_exiting = False
        self.enter_loop()

    def enter_loop(self):
        print("Entering the loop...")

    def loop_start(self):
        print("Starting loop iteration...")

    def loop_end(self):
        print("Ending loop iteration...")

    def exit_loop(self):
        print("Exiting the loop...")

    def __iter__(self):
        return self

    def __next__(self):
        if self.is_exiting:
            raise StopIteration

        try:
            self.loop_start()
            value = next(self.loop_iterable)
            self.loop_end()
            return value
        except StopIteration:
            self.exit_loop()
            self.is_exiting = True
            raise

def my_for(loop_iterable):
    it = MyIterator(loop_iterable)
    for item in it:
        yield item

# Example usage
for i in my_for([1, 2, 3]):
    print("i:", i)
    if i == 2:
        break  # loop_end and exit_loop will still execute
