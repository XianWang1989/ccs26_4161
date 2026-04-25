
class MyIterator:
    def __init__(self, loop_iterable):
        self.loop_iterable = loop_iterable
        self.iter = iter(loop_iterable)
        enter_loop()

    def __iter__(self):
        return self

    def __next__(self):
        try:
            loop_start()
            value = next(self.iter)
            return value
        finally:
            loop_end()

    def close(self):
        exit_loop()

# Example functions to demonstrate behavior
def enter_loop():
    print("Entering loop")

def loop_start():
    print("Loop start")

def loop_end():
    print("Loop end")

def exit_loop():
    print("Exiting loop")

# Usage of the custom iterator
try:
    for i in MyIterator([1, 2, 3]):
        print("i:", i)
        if i == 2:
            break
except StopIteration:
    pass
finally:
    # Ensure exit_loop is called when breaking the loop
    MyIterator([]).close()
